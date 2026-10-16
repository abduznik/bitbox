# tool: modpow
# description: Modular exponentiation a^b mod m
# author: @Enard52
# example: modpow "3" "4" "5" -> "1"


def run(*args) -> str:
    if len(args) != 3:
        return "Error: expected 3 arguments: a, b, m"

    try:
        a = int(str(args[0]).strip())
        b = int(str(args[1]).strip())
        m = int(str(args[2]).strip())
    except ValueError:
        return "Error: arguments must be integers"

    if m == 0:
        return "Error: modulus cannot be zero"
    if b < 0:
        return "Error: exponent must be non-negative"

    return str(pow(a, b, m))
