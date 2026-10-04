# tool: is_kaprekar
# description: Check if n is a Kaprekar number
# author: @abduznik
# example: is_kaprekar "9" -> "True"


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."
    try:
        n = int(str(args[0]).strip())
    except ValueError:
        return "Error: Argument must be an integer."
    if n < 1:
        return "False"
    square = str(n * n)
    for i in range(len(square)):
        right = square[i:]
        if int(right) == 0:  # a zero remainder makes every square trivially fit
            continue
        left = square[:i] or "0"
        if int(left) + int(right) == n:
            return "True"
    return "False"
