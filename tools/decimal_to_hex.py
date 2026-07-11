# tool: decimal_to_hex
# description: Converts a decimal integer to its hexadecimal string
# author: @chfr19820610-cell
# example: decimal_to_hex "255" -> "ff"

def run(*args) -> str:
    n = int(args[0])
    return hex(n)[2:]
