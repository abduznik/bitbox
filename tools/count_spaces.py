# tool: count_spaces
# description: Counts the number of spaces in a string.
# author: @navaneethsankar07
# example: count_spaces("hello world test") returns "2"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    return str(args[0].count(" "))
