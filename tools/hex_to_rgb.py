# tool: hex_to_rgb
# description: Converts a hex color code to RGB values
# author: @its-Sohan
# example: hex_to_rgb "#ff5733" -> "255, 87, 51"


def run(*args) -> str:
    hex_color = args[0].lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"{r}, {g}, {b}"
