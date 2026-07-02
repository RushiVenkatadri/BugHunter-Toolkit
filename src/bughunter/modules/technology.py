SERVER_SIGNATURES = {
    "nginx": "nginx",
    "apache": "Apache",
    "microsoft-iis": "Microsoft IIS",
    "iis": "Microsoft IIS",
    "litespeed": "LiteSpeed",
    "caddy": "Caddy",
    "openresty": "OpenResty",
    "envoy": "Envoy",
    "haproxy": "HAProxy",
    "github.com": "GitHub Pages"
}

POWERED_BY_SIGNATURES = {
    "php": "PHP",
    "asp.net": "ASP.NET",
    "express": "Express",
    "node": "Node.js",
    "laravel": "Laravel"
}

HEADER_SIGNATURES = {
    "cf-ray": "Cloudflare",
    "cf-cache-status": "Cloudflare",
    "x-vercel-id": "Vercel",
    "x-served-by": "Fastly",
    "x-amz-cf-id": "Amazon CloudFront",
    "x-amz-cf-pop": "Amazon CloudFront",
    "akamai-grn": "Akamai"
}


def detect_technologies(headers):

    technologies = []

    server = headers.get("Server", "").lower()

    powered = headers.get("X-Powered-By", "").lower()

    for signature, name in SERVER_SIGNATURES.items():

        if signature in server:
            technologies.append(name)

    for signature, name in POWERED_BY_SIGNATURES.items():

        if signature in powered:
            technologies.append(name)

    lower_headers = {
        key.lower(): value
        for key, value in headers.items()
    }

    for signature, name in HEADER_SIGNATURES.items():

        if signature in lower_headers:
            technologies.append(name)

    return sorted(set(technologies))
