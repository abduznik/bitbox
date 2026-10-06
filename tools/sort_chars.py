# tool: sort_chars
# description: Sorts the characters of a string.
# example: sort_chars cba returns "abc"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    return "".join(sorted(args[0]))