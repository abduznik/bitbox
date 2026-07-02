# tool: cube
# description: Returns the cube of a number
# author: @openclaw
# example: cube "3" -> "27"


def run(*args) -> str:
    n = float(args[0])
    result = n * n * n
    if result == int(result):
        result = int(result)
    return str(result)
