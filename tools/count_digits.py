# tool: count_digits
# description: Counts the number of digits in a string.
# author: @navaneethsankar07
# example: count_digits("abc123") returns "3"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    count = sum(char.isdigit() for char in args[0])
    return str(count)
