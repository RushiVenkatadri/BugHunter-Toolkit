import json
from pathlib import Path


def generate_json_report(
    domain,
    ip,
    response,
    findings,
    technologies,
    output_dir="results"
):
    data = {
        "target": domain,
        "ip_address": ip,
        "final_url": response.url,
        "status_code": response.status_code,
        "security_headers": findings,
        "technologies": technologies,
        "headers": dict(response.headers)
    }

    report = Path(output_dir) / domain / "report.json"

    with open(report, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

