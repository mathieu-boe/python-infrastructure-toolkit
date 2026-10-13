# Python Infrastructure Toolkit

A Python-based toolkit for infrastructure operations, built as part of my hands-on AWS and DevOps portfolio.

## Objectives

- Develop small, testable Python tools for infrastructure operations.
- Apply automated testing and code quality checks.
- Practise Linux, Git, and professional software development workflows.
- Build towards cloud operations and AWS automation use cases.

## Current status

**Milestone 1 — Initial project setup** (completed)

- [x] Python virtual environment created.
- [x] Initial package structure established.
- [x] First automated test passing.
- [x] `pyproject.toml` configured with project metadata and development dependencies.
- [x] CI pipeline configured with GitHub Actions.

**Milestone 2 — Initial CLI implementation** (completed)

- [x] Command-line interface implemented using Python's `argparse`.
- [x] Health command implemented.
- [x] Console command `infra-toolkit` configured.
- [x] Automated tests added for CLI behaviour and health checks.
- [x] Ruff linting and formatting checks configured.
- [x] All local quality checks passing.
- [x] GitHub Actions pipeline passing.

## Development

The project uses Python 3.14+, pytest, and Ruff. A local virtual environment is stored in `.venv/` and excluded from version control through `.gitignore`.

Clone the repository using SSH or HTTPS:

```bash
# SSH (requires an SSH key configured with GitHub)
git clone git@github.com:mathieu-boe/python-infrastructure-toolkit.git

# Alternatively, you can use HTTPS
git clone https://github.com/mathieu-boe/python-infrastructure-toolkit.git
```

Enter the project directory and create a virtual environment:

```bash
cd python-infrastructure-toolkit
python3 -m venv .venv
source .venv/bin/activate
```

Install the project in editable mode with its development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run the health check:

```bash
infra-toolkit health
```

Expected output:

```text
Status: operational
```

Display basic system information:

```bash
infra-toolkit system-info
```

Example output:

System Information
------------------
Operating system: Linux
Python version: 3.14.4
Architecture: x86_64

Note: The output reflects the environment where the command is executed, so values may differ across operating systems and machines.

Display available commands:

```bash
infra-toolkit --help
```

Run the quality checks and automated tests from the repository root:

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest -v
```

## Security and cost

The current development environment runs locally and does not require AWS resources/cloud expenditure.

No credentials, secrets, or generated virtual-environment files are to be committed.