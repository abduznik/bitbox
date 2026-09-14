# tool: fibonacci_nth
# description: Return the zero-indexed Fibonacci number F(n)
# author: @00200200
# example: fibonacci_nth "6" -> "8"


def run(*args) -> str:
    if len(args) != 1:
        raise ValueError("Requires exactly one argument")
    n = int(args[0])
    if n < 0:
        raise ValueError("Index must be nonnegative")
    # Fast doubling keeps the number of iterations logarithmic in n.
    current, following = 0, 1
    for bit in bin(n)[2:]:
        doubled = current * (2 * following - current)
        next_doubled = current * current + following * following
        if bit == "0":
            current, following = doubled, next_doubled
        else:
            current, following = next_doubled, doubled + next_doubled
    return str(current)
