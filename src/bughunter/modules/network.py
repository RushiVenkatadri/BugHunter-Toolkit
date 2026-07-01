import socket
import requests

def resolve_ip(domain: str):
    try:
        return socket.gethostbyname(domain)
    except Exception:
        return None

def fetch_website(domain: str):
    urls = [
        f"https://{domain}",
        f"http://{domain}"
    ]

    for url in urls:
        try:
            response = requests.get(
                url,
                timeout=10,
                allow_redirects=True,
                headers={
                    "User-Agent": "BugHunter Toolkit/1.0"
                }
            )

            return response

        except Exception:
            continue

    return None
def fetch_robots(domain: str):

    urls = [
        f"https://{domain}/robots.txt",
        f"http://{domain}/robots.txt"
    ]

    for url in urls:

        try:

            response = requests.get(
                url,
                timeout=10,
                headers={
                    "User-Agent": "BugHunter Toolkit/1.0"
                }
            )

            if response.status_code == 200:

                return response.text

        except Exception:
            continue

    return None
def fetch_sitemap(domain: str):

    urls = [
        f"https://{domain}/sitemap.xml",
        f"http://{domain}/sitemap.xml"
    ]

    for url in urls:

        try:

            response = requests.get(
                url,
                timeout=10,
                headers={
                    "User-Agent": "BugHunter Toolkit/1.0"
                }
            )

            if response.status_code == 200:

                return response.text

        except Exception:
            continue

    return None
def fetch_security_txt(domain: str):

    urls = [
        f"https://{domain}/.well-known/security.txt",
        f"https://{domain}/security.txt",
        f"http://{domain}/.well-known/security.txt",
        f"http://{domain}/security.txt"
    ]

    for url in urls:

        try:

            response = requests.get(
                url,
                timeout=10,
                headers={
                    "User-Agent": "BugHunter Toolkit/1.1"
                }
            )

            if response.status_code == 200:
                return response.text

        except Exception:
            continue

    return None
