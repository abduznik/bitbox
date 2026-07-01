# tool: is_even
# description: Checks if a number is even
# author: @insisong
# example: is_even "4" → "True"


def run(*args) -> str:
    n = int(args[0])
    return str(n % 2 == 0)
