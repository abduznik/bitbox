# tool: is_all_digits
# description: Checks whether a string contains only digits.
# author: @1998LJ
# example: is_all_digits "12345" -> "True"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    return str(str(args[0]).isdigit())
