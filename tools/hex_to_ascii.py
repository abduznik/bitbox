
# tool: hex_to_ascii
# description: decodes a hexadecimal string to ASCII text
# author: @Khushbu677
# example: hex_to_ascii "4869" -> "Hi"


def run(*args) -> str:
    if not args:
        return "Error: missing hexadecimal string"

    text = args[0]

    try:
        return bytes.fromhex(text).decode("ascii")
    except (ValueError, UnicodeDecodeError):
        return f"Error: '{text}' is not a valid hexadecimal string"
