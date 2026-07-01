from pathlib import Path

def generate_report(domain, ip, response):
    report = Path("results") / domain / "report.md"

    with open(report, "w", encoding="utf-8") as file:

        file.write("# BugHunter Toolkit Report\n\n")

        file.write(f"## Target\n{domain}\n\n")

        file.write(f"## IP Address\n{ip}\n\n")

        if response:

            file.write(f"## Final URL\n{response.url}\n\n")

            file.write(f"## Status Code\n{response.status_code}\n\n")

            file.write("## Response Headers\n\n")

            for key, value in response.headers.items():
                file.write(f"- **{key}**: {value}\n")
