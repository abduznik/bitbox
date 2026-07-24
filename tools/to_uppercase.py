# tool: to_uppercase
# description: Converts a string to uppercase.
# author: @navaneethsankar07
# example: to_uppercase("hello world") returns "HELLO WORLD"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    return args[0].upper()