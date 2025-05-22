# GitHub Secrets Detector

A security-focused tool to detect exposed API keys, secrets, and other sensitive information in GitHub repositories using regex-based scanning and GitHub API integration.

## Overview

**GitHub Secrets Detector** helps developers and organizations prevent the accidental exposure of sensitive credentials in public or private repositories. It performs automated scans using customizable regex patterns and supports integration with CI/CD pipelines and Docker environments.

## Tech Stack

* **Python 3.8+** – Core development language
* **GitHub API** – Repository access and metadata
* **Regex** – Pattern-based detection
* **Docker** – Containerized execution
* **GitHub Actions** – Optional CI integration
* **YAML** – User-defined configuration

## Features

* Automated repository scanning
* Regex-based secret detection (API keys, tokens, credentials, etc.)
* Customizable configuration via YAML
* Detailed scanning reports
* Docker support for isolated environments
* GitHub Actions integration (optional)

## Getting Started

### Prerequisites

* Python 3.8 or later
* GitHub account with a Personal Access Token
* `git` installed on your system

### Installation

```bash
git clone https://github.com/deepakgoudasirsi/github-secrets-detector.git
cd github-secrets-detector

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Configuration

Create a `config.yaml` file in the project root:

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

### Run the Scanner

```bash
python github_secrets_detector.py
```

## Docker Support

### Build the Docker Image

```bash
docker build -t github-secrets-detector .
```

### Run with Docker

```bash
docker run -v $(pwd)/config.yaml:/app/config.yaml github-secrets-detector
```

> Ensure `config.yaml` is mapped correctly when running in Docker.

---

## Contact

**Deepak Gouda**
GitHub: [@deepakgoudasirsi](https://github.com/deepakgoudasirsi)
LinkedIn: [linkedin.com/in/deepakgoudasirsi](https://linkedin.com/in/deepakgoudasirsi)
