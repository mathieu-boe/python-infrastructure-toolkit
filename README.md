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

**Milestone 4 — Resource usage monitoring** (completed)

- [x] Resource usage module implemented using `psutil`.
- [x] CPU, memory, and disk usage percentages reported.
- [x] `resource-usage` subcommand integrated into the `infra-toolkit` CLI.
- [x] Automated tests added for resource metrics and CLI output.
- [x] Resource collection tests use mocked metrics for deterministic results.
- [x] Ruff linting and formatting checks passing.
- [x] All 9 automated tests passing locally.

**Milestone 5 — Threshold-based resource monitoring** (completed)

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

**Milestone 6 — Configurable resource thresholds** (completed locally)

- [x] `--threshold` CLI argument added to the `resource-usage` command.
- [x] Default threshold remains 85%.
- [x] Custom integer and decimal thresholds supported.
- [x] Threshold values validated within the inclusive range of 0–100.
- [x] Non-numeric and out-of-range values rejected with clear CLI errors.
- [x] Warning output displays the configured threshold.
- [x] Automated tests added for custom thresholds and invalid input.
- [x] Ruff linting, formatting, and automated tests passing locally.

**Milestone 7 — JSON output and automation-ready exit codes** (implemented; local tests passing)

- [x] Optional `--json` argument added to the `resource-usage` command.
- [x] Structured JSON output includes resource measurements, threshold, status, and violations.
- [x] Human-readable output remains the default.
- [x] Exit code `0` returned when resource usage is within the configured threshold.
- [x] Exit code `1` returned when one or more resources exceed the threshold.
- [x] Invalid command-line arguments continue to use exit code `2`.
- [x] Automated tests added for healthy and threshold-exceeded JSON results.
- [x] Human-readable warning tests updated to verify exit code `1`.
- [x] All 21 automated tests passing locally.
- [ ] GitHub Actions pipeline verified for Milestone 7.

## Development

The project uses Python 3.14+, `psutil` for resource monitoring, pytest for automated testing, and Ruff for linting and formatting. A local virtual environment is stored in `.venv/` and excluded from version control through `.gitignore`.

### Clone the repository

Clone using SSH or HTTPS:

```bash
# SSH (requires an SSH key configured with GitHub)
git clone git@github.com:mathieu-boe/python-infrastructure-toolkit.git

# Alternatively, use HTTPS
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

### Health check

```bash
infra-toolkit health
```

Expected output:

```text
Status: operational
```

### System information

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

### Resource usage monitoring

Display current CPU, memory, and disk usage:

```bash
infra-toolkit resource-usage
```

The default warning threshold is 85%.

Example output:

```text
Resource Usage
--------------
CPU usage: 0.7%
Memory usage: 7.0%
Disk usage: 0.4%

Status: All resource usage is within thresholds.
```

*Note: These percentages are illustrative. Actual values depend on current system activity and the filesystem containing the current working directory.*

When any resource exceeds the threshold, the CLI displays a warning identifying the affected resources.

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

### Configurable thresholds

Override the default threshold using the `--threshold` argument:

```bash
infra-toolkit resource-usage --threshold 90
```

Decimal thresholds are also supported:

```bash
infra-toolkit resource-usage --threshold 87.5
```

The threshold must be between 0 and 100, inclusive. A warning is triggered only when resource usage **exceeds** the configured threshold; usage equal to the threshold does not trigger a warning.

Invalid values are rejected with a command-line error rather than a Python traceback. For example:

```bash
infra-toolkit resource-usage --threshold 101
```

```text
usage: infra-toolkit resource-usage [-h] [--threshold THRESHOLD] [--json]
infra-toolkit resource-usage: error: argument --threshold: Threshold must be between 0 and 100.
```

Another invalid input:

```bash
infra-toolkit resource-usage --threshold abc
```

```text
usage: infra-toolkit resource-usage [-h] [--threshold THRESHOLD] [--json]
infra-toolkit resource-usage: error: argument --threshold: Threshold must be a number between 0 and 100.
```

### JSON output

Use `--json` to produce structured output suitable for scripts and automation:

```bash
infra-toolkit resource-usage --json
```

Example output when all resources are within the threshold:

```json
{
  "cpu_percent": 25.0,
  "memory_percent": 60.0,
  "disk_percent": 75.0,
  "threshold": 85.0,
  "status": "ok",
  "violations": []
}
```

Use JSON with a custom threshold when needed:

```bash
infra-toolkit resource-usage --threshold 90 --json
```

Example output when CPU usage exceeds the threshold:

```json
{
  "cpu_percent": 92.0,
  "memory_percent": 60.0,
  "disk_percent": 88.0,
  "threshold": 90.0,
  "status": "threshold_exceeded",
  "violations": [
    "cpu_percent"
  ]
}
```

The `status` field is `ok` when no resource exceeds the threshold and `threshold_exceeded` otherwise. The `violations` list contains the keys of the resources that exceed the configured threshold.

### Exit codes

The `resource-usage` command uses exit codes so that scripts and CI pipelines can react to monitoring results.

| Exit code | Meaning |
|---|---|
| `0` | Monitoring completed; no threshold exceeded. |
| `1` | Monitoring completed; at least one threshold exceeded. |
| `2` | Invalid command-line arguments. |

The same monitoring exit codes apply to human-readable and JSON output. The `health` and `system-info` commands return `0` when successful.

### Command help

Display available resource monitoring options:

```bash
infra-toolkit resource-usage --help
```

Display all available commands:

```bash
infra-toolkit --help
```

### Run quality checks and automated tests

Run these commands from the repository root with the virtual environment activated:

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest -v
```

To apply automatic formatting:

```bash
python -m ruff format .
```

## Security and cost

The current development environment runs locally and does not require AWS resources or incur AWS infrastructure costs.

The toolkit reads local system resource metrics. No AWS credentials are required, and secrets or generated virtual-environment files must not be committed.
