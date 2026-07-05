# tool: divide
# description: Divides two numbers
# author: @its-Sohan
# example: divide "10" "3" -> "3.3333333333333335"


def run(*args) -> str:
    a, b = float(args[0]), float(args[1])
    return str(a / b)
