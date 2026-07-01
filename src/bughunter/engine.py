from bughunter.banner import show_banner

from bughunter.modules.output import success
from bughunter.modules.output import info
from bughunter.modules.output import warning
from bughunter.modules.output import error
from bughunter.modules.output import key_value
from bughunter.modules.output import workspace_tree
from bughunter.modules.output import security_report

from bughunter.modules.validator import validate_domain
from bughunter.modules.workspace import create_workspace
from bughunter.modules.workspace import save_raw_file

from bughunter.modules.network import resolve_ip
from bughunter.modules.network import fetch_website
from bughunter.modules.network import fetch_robots
from bughunter.modules.network import fetch_sitemap

from bughunter.modules.security import analyze_headers
from bughunter.modules.reporter import generate_report


def run_scan(domain):

    show_banner()

    info(f"Target: {domain}")

    if not validate_domain(domain):
        error("Invalid domain")
        return

    success("Domain Valid")

    create_workspace(domain)

    success("Workspace Created")

    ip = resolve_ip(domain)

    key_value("IP Address", ip)

    info("Connecting...")

    response = fetch_website(domain)

    if response is None:
        error("Unable to connect")
        return

    key_value("Status", response.status_code)
    key_value("Final URL", response.url)

    findings = analyze_headers(response.headers)

    security_report(findings)

    robots = fetch_robots(domain)

    if robots:
        save_raw_file(domain, "robots.txt", robots)
        success("robots.txt Downloaded")
    else:
        warning("robots.txt Not Found")

    sitemap = fetch_sitemap(domain)

    if sitemap:
        save_raw_file(domain, "sitemap.xml", sitemap)
        success("sitemap.xml Downloaded")
    else:
        warning("sitemap.xml Not Found")

    generate_report(domain, ip, response)

    success("Markdown Report Generated")

    workspace_tree(domain)

    success("Recon Finished")
