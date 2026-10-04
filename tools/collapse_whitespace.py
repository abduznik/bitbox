# tool: collapse_whitespace
# description: Collapse all whitespace to single spaces and trim
# author: @abduznik
# example: collapse_whitespace "  hello   world  " -> "hello world"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."
    return " ".join(str(args[0]).split())
