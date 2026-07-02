import argparse

from bughunter.engine import run_scan

VERSION = "1.2.0"


def main():

    parser = argparse.ArgumentParser(
        prog="bughunter",
        description="BugHunter Toolkit - Modular Bug Bounty Reconnaissance CLI"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="""BugHunter Toolkit v1.2.0
        Author : Rushi Venkatadri
        GitHub : https://github.com/RushiVenkatadri"""
    )

    subparsers = parser.add_subparsers(
        dest="command",
        metavar="<command>"
    )

    scan = subparsers.add_parser(
        "scan",
        help="Scan a target domain"
    )

    scan.add_argument(
        "domain",
        help="Target domain (example: nasa.gov)"
    )

    scan.add_argument(
        "-o",
        "--output",
        metavar="DIR",
        default="results",
        help="Directory to save scan results (default: results)"
    )

    args = parser.parse_args()

    if args.command == "scan":
        run_scan(args.domain, args.output)
    else:
        parser.print_help()
