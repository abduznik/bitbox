# tool: hex_to_decimal
# description: Converts a hexadecimal string to its decimal integer value
# author: @chfr19820610-cell
# example: hex_to_decimal "ff" -> "255"

def run(*args) -> str:
    hex_str = args[0]
    return str(int(hex_str, 16))
