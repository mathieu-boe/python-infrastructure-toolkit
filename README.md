# Python Infrastructure Toolkit

A Python-based toolkit for infrastructure operations, built as part of my hands-on AWS and DevOps portfolio.

## Objectives

- Develop small, testable Python tools for infrastructure operations.
- Apply automated testing and code quality checks.
- Practise Linux, Git, and professional software development workflows.
- Build towards cloud operations and AWS automation use cases.

## Current status

**Milestone 1 — Initial project setup**

- [x] Python virtual environment created.
- [x] Initial package structure established.
- [x] First automated test passing.
- [ ] Configure pyproject.toml.
- [ ] CI pipeline configured.
- [ ] First infrastructure utility implemented.

## Development

The project uses Python and pytest. A local virtual environment is stored in `.venv/` and excluded from version control through
.venv/
venv/
in .gitgnore.

To install the project in editable mode and run the tests from the repository root:

```bash
python -m pip install -e ".[dev]"
python -m pytest tests/test_health.py -v
```

Note: ~~We don't have a pyproject.toml yet, run tests with PYTHONPATH=src ./.venv/bin/python -m pytest tests/test_health.py -v to ensure Python can locate the infra_toolkit package.~~


## Security and cost

The initial development environment runs locally and does not require AWS resources/cloud expenditure.

No credentials, secrets, or generated virtual-environment files are to be committed.