# tool: fibonacci
# description: Returns the nth Fibonacci number
# author: @its-Sohan
# example: fibonacci "10" -> "55"


def run(*args) -> str:
    n = int(args[0])
    if n <= 0:
        return "0"
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return str(b)
