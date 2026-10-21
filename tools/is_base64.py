# tool: is_base64
# description: Checks whether a string is valid canonical Base64
# author: @Doomguy-BFG9000
# example: is_base64 "aGVsbG8=" -> "True"

import base64
import binascii


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Requires exactly one argument"

    text = args[0]
    if not text:
        return "False"

    try:
        encoded = text.encode("ascii")
        decoded = base64.b64decode(encoded, validate=True)
    except (UnicodeEncodeError, binascii.Error, ValueError):
        return "False"

    return str(base64.b64encode(decoded) == encoded)
