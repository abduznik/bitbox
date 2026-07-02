# tool: first_char
# description: Returns the first character of a string
# author: @navaneethsankar07
# example: first_char "hello" → "h"


def run(*args) -> str:
    text = args[0]
    return text[0] if text else ""