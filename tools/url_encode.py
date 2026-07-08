# tool: url_encode
# description: Percent-encodes text for use in URLs
# author: @blackkingwow
# example: url_encode "hello world&foo" -> "hello+world%26foo"


def run(*args) -> str:
    from urllib.parse import quote_plus

    text = args[0]
    return quote_plus(text)
