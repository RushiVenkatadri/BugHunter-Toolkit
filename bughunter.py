import sys

from banner import show_banner
from modules.output import success
from modules.output import error
from modules.output import info
from modules.output import workspace_tree
from modules.validator import validate_domain
from modules.workspace import create_workspace


def main():

    show_banner()

    if len(sys.argv) != 2:
        error("Usage: python3 bughunter.py <domain>")
        return

    domain = sys.argv[1]

    info(f"Target: {domain}")

    if not validate_domain(domain):
        error("Invalid Domain")
        return

    success("Domain Valid")

    info("Creating Workspace...")

    create_workspace(domain)

    success("Workspace Created")

    workspace_tree(domain)

    success("Ready for Recon")


if __name__ == "__main__":
    main()
