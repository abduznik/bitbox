# tool: hex_to_rgb
# description: converts a hex color to RGB components
# author: @Solaris-star
# example: hex_to_rgb "#ff8800" -> "255,136,0"

import re


def run(*args) -> str:
    if not args:
        return "Error: expected a hex color"
    value = args[0].strip().lstrip("#")
    if not re.fullmatch(r"[0-9a-fA-F]{3}|[0-9a-fA-F]{6}", value):
        return f"Error: '{args[0]}' is not a valid hex color"
    if len(value) == 3:
        value = "".join(ch * 2 for ch in value)
    r = int(value[0:2], 16)
    g = int(value[2:4], 16)
    b = int(value[4:6], 16)
    return f"{r},{g},{b}"
