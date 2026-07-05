# tool: power
# description: Raises a number to a power
# author: @its-Sohan
# example: power "2" "3" -> "8"


def run(*args) -> str:
    base, exp = float(args[0]), float(args[1])
    result = base ** exp
    if result == int(result):
        result = int(result)
    return str(result)
