# tool: decimal_to_hex
# description: Converts a decimal integer to its hexadecimal string
# author: @Evarline
# example: decimal_to_hex "255" -> "ff"


# Define a function named 'run' that accepts multiple inputs (*args) and outputs a string (-> str)
def run(*args) -> str:
    if not args or args[0] is None:
        return ""

    raw = args[0]

    try:
        s = str(raw).strip()
        try:
            val = int(s)
        except ValueError:
            val = int(float(s))
    except (ValueError, TypeError, OverflowError):  # Convert to float first, then to int
        return ""

    is_negative = val < 0
    val = abs(val)
    hex_str = hex(val)[2:]  # Convert to hex and remove '0x' prefix

    return f"-{hex_str}" if is_negative else hex_str