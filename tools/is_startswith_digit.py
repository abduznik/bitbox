# tool: is_startswith_digit
# description: Checks whether a string starts with a digit.
# author: @1998LJ
# example: is_startswith_digit "1st place" -> "True"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    text = str(args[0])
    return str(bool(text) and text[0].isdigit())
