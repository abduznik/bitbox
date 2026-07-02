# tool: last_char
# description: Returns the last character of a string
# author: @navaneethsankar07
# example: last_char("hello") returns "o"


def run(*args) -> bool:
    string = args[0]
    return string[-1] if string else ""