# tool: decimal_to_hex
# description: Converts a decimal integer to its hexadecimal string
# author: @Evarline
# example: decimal_to_hex "255" -> "ff"


# Define a function named 'run' that accepts multiple inputs (*args) and outputs a string (-> str)
def run(*args) -> str:
    if not args or args[0] is None:
        return ""

    try:
        val = int(float(str(args[0]).strip()))
    except (ValueError, TypeError):
        return ""

    if val < 0:
        return f"-{abs(val):x}"
    return f"{val:x}"