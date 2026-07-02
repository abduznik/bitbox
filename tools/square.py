# tool: square
# description: Returns the square of a number
# author: @openclaw
# example: square "5" -> "25"


def run(*args) -> str:
    n = float(args[0])
    result = n * n
    if result == int(result):
        result = int(result)
    return str(result)
