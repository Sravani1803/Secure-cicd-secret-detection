# CI/CD Security Pipeline for Secret Detection

## Project Overview
This project demonstrates how a CI/CD pipeline can automatically detect hardcoded secrets in source code and prevent insecure builds from progressing.

## Threat Addressed
Hardcoded secrets exposure in application source code, including API keys, passwords, and tokens.

## Objective
To integrate automated secret scanning into a GitHub Actions pipeline so that insecure commits are identified during development and blocked before deployment.

## Tools Used
- Python
- Flask
- Pytest
- GitHub Actions
- Gitleaks

## Workflow
1. Developer pushes code to GitHub
2. GitHub Actions starts automatically
3. Dependencies are installed
4. Unit tests run
5. Gitleaks scans the repository for secrets
6. If a secret is found, the pipeline fails
7. If no secret is found, the pipeline passes

## Real Time Security Result
This project provides near real-time validation because every code push triggers an automated security check and immediately shows whether the build is safe or blocked.

## Example Outcome
- Insecure commit with hardcoded secret: pipeline failed
- Secure commit using environment variables: pipeline passed

## Business Value
This project demonstrates shift-left security by identifying credential exposure early in the software development lifecycle and reducing the risk of insecure code deployment.
