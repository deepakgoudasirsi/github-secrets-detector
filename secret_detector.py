#!/usr/bin/env python3

import os
import re
import json
import argparse
from pathlib import Path
from typing import List, Dict, Set
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SecretDetector:
    def __init__(self, config_path: str = "patterns.json"):
        """Initialize the secret detector with regex patterns."""
        self.patterns = self._load_patterns(config_path)
        self.found_secrets: Dict[str, List[Dict]] = {}
        
    def _load_patterns(self, config_path: str) -> Dict[str, str]:
        """Load regex patterns from configuration file."""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Pattern configuration file not found: {config_path}")
            return {}
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in pattern configuration file: {config_path}")
            return {}

    def scan_file(self, file_path: str) -> List[Dict]:
        """Scan a single file for secrets."""
        secrets_found = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            for pattern_name, pattern in self.patterns.items():
                matches = re.finditer(pattern, content)
                for match in matches:
                    secret = {
                        'pattern_name': pattern_name,
                        'line_number': content[:match.start()].count('\n') + 1,
                        'match': match.group(),
                        'context': self._get_context(content, match.start(), match.end())
                    }
                    secrets_found.append(secret)
                    
        except Exception as e:
            logger.error(f"Error scanning file {file_path}: {str(e)}")
            
        return secrets_found

    def _get_context(self, content: str, start: int, end: int, context_lines: int = 2) -> str:
        """Get surrounding context for a matched secret."""
        lines = content.split('\n')
        line_number = content[:start].count('\n')
        
        start_line = max(0, line_number - context_lines)
        end_line = min(len(lines), line_number + context_lines + 1)
        
        context = []
        for i in range(start_line, end_line):
            prefix = '>' if i == line_number else ' '
            context.append(f"{prefix} {i+1}: {lines[i]}")
            
        return '\n'.join(context)

    def scan_directory(self, directory: str, exclude_dirs: Set[str] = None) -> Dict[str, List[Dict]]:
        """Scan a directory recursively for secrets."""
        if exclude_dirs is None:
            exclude_dirs = {'.git', '__pycache__', 'node_modules', 'venv'}
            
        for root, dirs, files in os.walk(directory):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                file_path = os.path.join(root, file)
                secrets = self.scan_file(file_path)
                if secrets:
                    self.found_secrets[file_path] = secrets
                    
        return self.found_secrets

    def generate_report(self, output_file: str = None) -> str:
        """Generate a report of found secrets."""
        if not self.found_secrets:
            return "No secrets found."
            
        report = []
        report.append("=== GitHub Secrets Detection Report ===\n")
        
        for file_path, secrets in self.found_secrets.items():
            report.append(f"\nFile: {file_path}")
            for secret in secrets:
                report.append(f"\n  Pattern: {secret['pattern_name']}")
                report.append(f"  Line: {secret['line_number']}")
                report.append(f"  Match: {secret['match']}")
                report.append("  Context:")
                report.append(secret['context'])
                report.append("-" * 50)
                
        report_text = "\n".join(report)
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(report_text)
                
        return report_text

def main():
    parser = argparse.ArgumentParser(description="GitHub Secrets Detector")
    parser.add_argument("directory", help="Directory to scan for secrets")
    parser.add_argument("--config", default="patterns.json", help="Path to pattern configuration file")
    parser.add_argument("--output", help="Path to output report file")
    parser.add_argument("--exclude", nargs="+", help="Additional directories to exclude")
    
    args = parser.parse_args()
    
    exclude_dirs = {'.git', '__pycache__', 'node_modules', 'venv'}
    if args.exclude:
        exclude_dirs.update(args.exclude)
    
    detector = SecretDetector(args.config)
    detector.scan_directory(args.directory, exclude_dirs)
    report = detector.generate_report(args.output)
    
    if args.output:
        logger.info(f"Report written to {args.output}")
    else:
        print(report)

if __name__ == "__main__":
    main() 