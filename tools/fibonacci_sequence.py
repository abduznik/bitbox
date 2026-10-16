# tool: fibonacci_sequence
# description: First n Fibonacci numbers
# author: @Enard52
# example: fibonacci_sequence "6" -> "0,1,1,2,3,5"


def run(*args) -> str:
    if not args:
        return "Error: expected an integer"
    val = str(args[0]).strip()
    if not val:
        return "Error: expected an integer"

    try:
        n = int(val)
    except ValueError:
        return "Error: argument must be an integer"

    if n < 0:
        return "Error: argument must be a non-negative integer"
    if n == 0:
        return ""
    if n == 1:
        return "0"

    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])

    return ",".join(str(x) for x in seq)
