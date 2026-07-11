# tool: octal_to_decimal
# description: Converts an octal string to its decimal integer value
# author: @chfr19820610-cell
# example: octal_to_decimal "77" -> "63"

def run(*args) -> str:
    octal = args[0]
    return str(int(octal, 8))
