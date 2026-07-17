# tool: url_decode
# description: Decodes a percent-encoded URL string
# author: @navaneethsankar07
# example: url_decode "hello+world" -> "hello world"


from urllib.parse import unquote_plus


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    return unquote_plus(args[0])