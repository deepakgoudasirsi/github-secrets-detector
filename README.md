# 🔍 GitHub Secrets Detector

A powerful tool to detect exposed API keys, secrets, and sensitive information in GitHub repositories using advanced regex patterns and automated scanning capabilities.

## 📋 Overview

GitHub Secrets Detector is a security-focused tool that helps developers and organizations identify and prevent accidental exposure of sensitive information in their GitHub repositories. It uses a combination of regex patterns and advanced scanning techniques to detect various types of secrets, API keys, and credentials that might have been committed to the repository.

## 🛠️ Tech Stack

- **Python 3.8+**: Core programming language
- **GitHub API**: Repository access and scanning
- **Regex Patterns**: Pattern matching for secrets detection
- **GitHub Actions**: CI/CD integration
- **Docker**: Containerization support
- **YAML**: Configuration management

## ✨ Features

- 🔍 **Automated Scanning**: Scan repositories for exposed secrets and API keys
- 🎯 **Pattern Detection**: Detect various types of secrets using regex patterns
- 🔄 **CI/CD Integration**: Seamless integration with GitHub Actions
- 📊 **Detailed Reports**: Generate comprehensive reports of findings
- 🛡️ **Security Focus**: Help prevent security breaches and data leaks
- 🔌 **Extensible**: Easy to add new patterns and detection rules
- 🐳 **Docker Support**: Run in containerized environments
- 📝 **Configurable**: Customize scanning rules and patterns

## 🚀 How to Run

### Prerequisites

- Python 3.8 or higher
- Git
- GitHub account (for repository access)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/github-secrets-detector.git
cd github-secrets-detector
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

1. Configure your GitHub token in `config.yaml`:
```yaml
github:
  token: "your_github_token"
```

2. Run the scanner:
```bash
python github_secrets_detector.py
```

### Docker Usage

1. Build the Docker image:
```bash
docker build -t github-secrets-detector .
```

2. Run the container:
```bash
docker run -v $(pwd)/config.yaml:/app/config.yaml github-secrets-detector
```


## 🔧 Configuration

The tool can be configured through `config.yaml`:

```yaml
github:
  token: "your_github_token"
  api_url: "https://api.github.com"

scanning:
  patterns:
    - name: "AWS Access Key"
      pattern: "AKIA[0-9A-Z]{16}"
    - name: "GitHub Token"
      pattern: "ghp_[a-zA-Z0-9]{36}"
```
