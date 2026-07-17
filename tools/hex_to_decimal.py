# tool: hex_to_decimal
# description: converts hexadecimal to decimal value
# author: @persianflower
# example: hex_to_decimal "ff" -> "255"


def run(*args) -> str:
    try:
        return str(int(args[0], 16))
    except (ValueError, IndexError):
        return f"Error: '{args[0]}' is not a valid hexadecimal string"
