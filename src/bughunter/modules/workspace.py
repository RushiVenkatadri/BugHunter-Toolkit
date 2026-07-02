from pathlib import Path

def create_workspace(domain: str, output_dir: str = "results"):
    base = Path(output_dir) / domain
    raw = base / "raw"

    raw.mkdir(parents=True, exist_ok=True)

    (base / "report.md").touch(exist_ok=True)
    (base / "logs.txt").touch(exist_ok=True)

    return base

def save_raw_file(domain: str, filename: str, content: str, output_dir: str = "results"):

    if content is None:
        return

    file = Path(output_dir) / domain / "raw" / filename

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
