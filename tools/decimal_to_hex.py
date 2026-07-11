# tool: decimal_hex
# description: Converts a decimal integer to its hexadecimal string
# author: @Evarline
# example: decimal_to_hex "255 -> "ff"


def run(*args) -> str:
    n = args[0]
    return hex(int(n))[2: ]
