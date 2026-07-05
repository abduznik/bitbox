# tool: modulo
# description: Returns the remainder of dividing two numbers
# author: @its-Sohan
# example: modulo "10" "3" -> "1"


def run(*args) -> str:
    a, b = int(args[0]), int(args[1])
    return str(a % b)
