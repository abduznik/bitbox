# tool: count_special_chars
# description: Counts the number of special (non-alphanumeric) characters.
# author: @navaneethsankar07
# example: count_special_chars("hello!@#") returns "3"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    count = sum(not char.isalnum() for char in args[0])
    return str(count)
