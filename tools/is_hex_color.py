# tool: is_hex_color
# description: Validate CSS hex colors (#RGB, #RGBA, #RRGGBB or #RRGGBBAA)
# author: @00200200
# example: is_hex_color "#FF5733" -> "True"

import re


def run(*args) -> str:
    if len(args) != 1:
        raise ValueError("Requires exactly one argument")
    return str(
        re.fullmatch(
            r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})", args[0]
        )
        is not None
    )
