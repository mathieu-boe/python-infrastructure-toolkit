import argparse

from infra_toolkit.health import check_status
from infra_toolkit.system_info import get_system_info


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="infra-toolkit",
        description="A toolkit for infrastructure operations.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("health", help="Check toolkit health")
    subparsers.add_parser("system-info", help="Display system information")

    args = parser.parse_args()

    if args.command == "health":
        print(f"Status: {check_status()}")

    elif args.command == "system-info":
        info = get_system_info()
        print("System Information")
        print("------------------")
        print(f"Operating system: {info['operating_system']}")
        print(f"Python version: {info['python_version']}")
        print(f"Architecture: {info['architecture']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
