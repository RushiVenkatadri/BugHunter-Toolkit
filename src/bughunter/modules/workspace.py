from pathlib import Path

def create_workspace(domain: str):
    base = Path("results") / domain
    raw = base / "raw"

    raw.mkdir(parents=True, exist_ok=True)

    (base / "report.md").touch(exist_ok=True)
    (base / "logs.txt").touch(exist_ok=True)

    return base

def save_raw_file(domain: str, filename: str, content: str):

    if content is None:
        return

    file = Path("results") / domain / "raw" / filename

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
