# tool: rgb_to_hex
# description: Converts RGB values to a hex color code
# author: @its-Sohan
# example: rgb_to_hex "255" "87" "51" -> "#ff5733"


def run(*args) -> str:
    r, g, b = int(args[0]), int(args[1]), int(args[2])
    return f"#{r:02x}{g:02x}{b:02x}"
