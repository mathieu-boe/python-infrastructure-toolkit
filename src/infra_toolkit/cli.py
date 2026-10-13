import argparse

from infra_toolkit.health import check_status
from infra_toolkit.resource_usage import get_resource_usage
from infra_toolkit.system_info import get_system_info
from infra_toolkit.thresholds import find_threshold_violations


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="infra-toolkit",
        description="A toolkit for infrastructure operations.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("health", help="Check toolkit health")
    subparsers.add_parser("system-info", help="Display system information")
    subparsers.add_parser("resource-usage", help="Display resource usage")

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

    elif args.command == "resource-usage":
        usage = get_resource_usage()
        violations = find_threshold_violations(usage)

        print("Resource Usage")
        print("--------------")
        #:.1f formatting displays each percentage to one decimal place
        print(f"CPU usage: {usage['cpu_percent']:.1f}%")
        print(f"Memory usage: {usage['memory_percent']:.1f}%")
        print(f"Disk usage: {usage['disk_percent']:.1f}%")

        if violations:
            print()
            print("WARNING: Resource usage threshold exceeded (85%).")

            resource_labels = {
                "cpu_percent": "CPU",
                "memory_percent": "Memory",
                "disk_percent": "Disk",
            }

            for resource in violations:
                print(f"- {resource_labels[resource]}")
        else:
            print()
            print("Status: All resource usage is within thresholds.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
