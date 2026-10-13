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

**Milestone 3 — System information command** (completed)

- [x] System information module implemented using Python's `platform` standard library.
- [x] Operating system, Python version, and machine architecture reported.
- [x] `system-info` subcommand integrated into the `infra-toolkit` CLI.
- [x] Automated tests added for system information and CLI output.
- [x] Ruff linting and formatting checks passing.
- [x] All 6 automated tests passing.
- [x] GitHub Actions pipeline passing.

**Milestone 4 — Resource usage monitoring** (implemented; local checks passing)

- [x] Resource usage module implemented using `psutil`.
- [x] CPU, memory, and disk usage percentages reported.
- [x] `resource-usage` subcommand integrated into the `infra-toolkit` CLI.
- [x] Automated tests added for resource metrics and CLI output.
- [x] Resource collection tests use mocked metrics for deterministic results.
- [x] Ruff linting and formatting checks passing.
- [x] All 9 automated tests passing locally.

**Milestone 5 — Threshold-based resource monitoring** (implemented; local checks passing)

- [x] Reusable threshold evaluation function implemented in `thresholds.py`.
- [x] Default resource usage threshold set to 85%.
- [x] CPU, memory, and disk usage checked against the threshold.
- [x] Terminal warning displayed when one or more resources exceed the threshold.
- [x] Names of resources exceeding the threshold displayed in the warning.
- [x] Invalid threshold values rejected by the threshold evaluation function.
- [x] Automated tests added for threshold evaluation and CLI warning behaviour.
- [x] Ruff linting and formatting checks passing.
- [x] All 15 automated tests passing locally.
- [x] GitHub Actions pipeline passing.

## Development

The project uses Python 3.14+, `psutil` for resource monitoring, pytest for automated testing, and Ruff for linting and formatting. A local virtual environment is stored in `.venv/` and excluded from version control through `.gitignore`.

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

```text
System Information
------------------
Operating system: Linux
Python version: 3.14.4
Architecture: x86_64
```

*Note: The output reflects the environment where the command is executed, so values may differ across operating systems and machines.*

Display current CPU, memory, and disk usage:

```bash
infra-toolkit resource-usage
```

Example output:

```text
Resource Usage
--------------
CPU usage: 0.7%
Memory usage: 7.0%
Disk usage: 0.4%
```

*Note: These percentages are illustrative. Actual values depend on current system activity and the filesystem containing the current working directory.*

When CPU, memory, or disk usage exceeds the default threshold of 85%, the CLI displays a warning identifying the affected resources.

Example warning output:

```text
Resource Usage
--------------
CPU usage: 92.0%
Memory usage: 60.0%
Disk usage: 88.0%

WARNING: Resource usage threshold exceeded (85%).
- CPU
- Disk
```

If no resource exceeds the threshold, the CLI reports that all resource usage is within thresholds. The threshold is currently fixed at 85% in the CLI; configurable command-line thresholds are not implemented yet.

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