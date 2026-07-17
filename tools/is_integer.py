# tool: is_integer
# description: checks if a given input is an integer
# author: @navaneethsankar07
# example: is_integer "-42" -> "True"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    try:
        int(args[0])
        return "True"
    except ValueError:
        return "False"
