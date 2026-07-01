import re

def validate_domain(domain: str) -> bool:
    pattern = re.compile(
        r"^(?!-)(?:[A-Za-z0-9-]{1,63}\.)+[A-Za-z]{2,63}$"
    )
    return bool(pattern.fullmatch(domain))
