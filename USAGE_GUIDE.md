# GitHub Secrets Detector - Comprehensive Usage Guide

## Table of Contents
1. [Setup](#setup)
2. [Basic Usage](#basic-usage)
3. [Advanced Usage](#advanced-usage)
4. [CI/CD Integration](#cicd-integration)
5. [Custom Patterns](#custom-patterns)
6. [Understanding Results](#understanding-results)
7. [Troubleshooting](#troubleshooting)

## Setup

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Git (for version control)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/github-secrets-detector.git
cd github-secrets-detector
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows
# venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Make the script executable:
```bash
chmod +x secret_detector.py
```

## Basic Usage

### Scan a Directory
```bash
python secret_detector.py /path/to/scan
```

### Generate Report File
```bash
python secret_detector.py /path/to/scan --output report.txt
```

### Exclude Directories
```bash
python secret_detector.py /path/to/scan --exclude dist build node_modules
```

## Advanced Usage

### Custom Configuration
1. Create a custom patterns file (e.g., `custom_patterns.json`)
2. Run with custom configuration:
```bash
python secret_detector.py /path/to/scan --config custom_patterns.json
```

### Scanning Specific File Types
The tool automatically scans all files. To scan specific file types, use the `--include` option:
```bash
python secret_detector.py /path/to/scan --include "*.py" "*.js" "*.env"
```

### Verbose Output
For detailed logging:
```bash
python secret_detector.py /path/to/scan --verbose
```

## CI/CD Integration

### GitHub Actions
1. Copy `.github/workflows/secret-scan.yml` to your repository
2. The workflow will run automatically on:
   - Push to main/master
   - Pull requests
   - Daily at midnight

### Custom CI/CD Pipeline
Add these steps to your pipeline:
```yaml
- name: Install Python
  uses: actions/setup-python@v4
  with:
    python-version: '3.9'

- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt

- name: Run secret scanner
  run: |
    python secret_detector.py . --output scan_report.txt
```

## Custom Patterns

### Pattern Format
Patterns are defined in JSON format:
```json
{
    "PATTERN_NAME": "regex_pattern",
    "ANOTHER_PATTERN": "another_regex"
}
```

### Adding New Patterns
1. Edit `patterns.json` or create a new file
2. Add your pattern with a descriptive name
3. Use the `--config` option to use your patterns

### Pattern Examples
```json
{
    "API_KEY": "api[_-]?key[_-]?[a-zA-Z0-9]{32,}",
    "PASSWORD": "password[_-]?[a-zA-Z0-9@#$%^&*()_+]{8,}"
}
```

## Understanding Results

### Report Format
```
=== GitHub Secrets Detection Report ===

File: /path/to/file
  Pattern: PATTERN_NAME
  Line: 42
  Match: found_secret
  Context:
   40: some code
> 42: secret = "found_secret"
   44: more code
--------------------------------------------------
```

### Interpreting Results
- **Pattern**: Type of secret found
- **Line**: Line number in the file
- **Match**: The actual secret found
- **Context**: Surrounding code for context

## Troubleshooting

### Common Issues

1. **No patterns found**
   - Check if `patterns.json` exists
   - Verify JSON format is correct
   - Check file permissions

2. **Scan too slow**
   - Use `--exclude` to skip directories
   - Use `--include` to scan specific files
   - Check for large binary files

3. **False positives**
   - Adjust pattern regex
   - Add more context to patterns
   - Use `--exclude` for test files

### Debug Mode
For detailed debugging:
```bash
python secret_detector.py /path/to/scan --debug
```

## Best Practices

1. **Regular Scanning**
   - Run scans before commits
   - Use CI/CD integration
   - Schedule regular scans

2. **Pattern Management**
   - Keep patterns updated
   - Add organization-specific patterns
   - Review and update regularly

3. **Security**
   - Don't commit real secrets
   - Use environment variables
   - Rotate secrets regularly

4. **Performance**
   - Exclude unnecessary directories
   - Use specific file patterns
   - Regular maintenance

## Support

For issues and feature requests:
1. Check the documentation
2. Review common issues
3. Submit a GitHub issue
4. Contact the maintainers 