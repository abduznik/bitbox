# tool: is_url
# description: checks whether a string looks like an HTTP/HTTPS URL
# author: @Solaris-star
# example: is_url "https://example.com" -> "true"

from urllib.parse import urlparse


def run(*args) -> str:
    if not args:
        return "Error: expected a string argument"
    value = args[0].strip()
    try:
        parsed = urlparse(value)
    except Exception:
        return "false"
    if parsed.scheme not in {"http", "https"}:
        return "false"
    if not parsed.netloc:
        return "false"
    return "true"

