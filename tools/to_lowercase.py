# tool: to_lowercase
# description: Converts the input string to lowercase
# author: @navaneethsankar07
# example: to_lowercase "HELLO WORLD" -> "hello world"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    return args[0].lower()