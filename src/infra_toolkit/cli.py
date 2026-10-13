import argparse

from infra_toolkit.health import check_status


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="infra-toolkit",
        description="A toolkit for infrastructure operations.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("health", help="Check toolkit health")

    args = parser.parse_args()

    if args.command == "health":
        print(f"Status: {check_status()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
