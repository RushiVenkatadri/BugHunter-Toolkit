import argparse

from bughunter.engine import run_scan

def main():

    parser = argparse.ArgumentParser(
        prog="bughunter",
        description="BugHunter Toolkit"
    )

    subparsers = parser.add_subparsers(dest="command")

    scan = subparsers.add_parser(
        "scan",
        help="Run reconnaissance against a domain"
    )

    scan.add_argument("domain")

    args = parser.parse_args()

    if args.command == "scan":
        run_scan(args.domain)
    else:
        parser.print_help()
