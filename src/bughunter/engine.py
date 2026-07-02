from bughunter.banner import show_banner

from bughunter.modules.output import success
from bughunter.modules.output import info
from bughunter.modules.output import warning
from bughunter.modules.output import error
from bughunter.modules.output import key_value
from bughunter.modules.output import workspace_tree
from bughunter.modules.output import security_report
from bughunter.modules.network import fetch_sitemap
from bughunter.modules.network import fetch_security_txt
from bughunter.modules.validator import validate_domain
from bughunter.modules.workspace import create_workspace
from bughunter.modules.workspace import save_raw_file

from bughunter.modules.network import resolve_ip
from bughunter.modules.network import fetch_website
from bughunter.modules.network import fetch_robots
from bughunter.modules.network import fetch_sitemap

from bughunter.modules.security import analyze_headers
from bughunter.modules.reporter import generate_report
from bughunter.modules.json_report import generate_json_report
from bughunter.modules.html_report import generate_html_report


def run_scan(domain, output_dir="results"):
    show_banner()

    info(f"Target: {domain}")

    if not validate_domain(domain):
        error("Invalid domain")
        return

    success("Domain Valid")

    create_workspace(domain,output_dir)

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
        save_raw_file(domain, "robots.txt", robots, output_dir)
        success("robots.txt Downloaded")
    else:
        warning("robots.txt Not Found")

    sitemap = fetch_sitemap(domain)

    if sitemap:
        save_raw_file(domain, "sitemap.xml", sitemap, output_dir)
        success("sitemap.xml Downloaded")
    else:
        warning("sitemap.xml Not Found")

    security_txt = fetch_security_txt(domain)

    if security_txt:
           save_raw_file(domain, "security.txt", security_txt,output_dir)
           success("security.txt Downloaded")
    else:
           warning("security.txt Not Found")


    generate_report(domain, ip, response,output_dir)

    success("Markdown Report Generated")

    generate_json_report(
       domain,
       ip,
       response,
       findings,
       output_dir
    )

    success("JSON Report Generated")

    generate_html_report(
       domain,
       ip,
       response,
       findings,
       output_dir
    )

    success("HTML Report Generated")



    workspace_tree(domain,output_dir)

    success("Recon Finished")
