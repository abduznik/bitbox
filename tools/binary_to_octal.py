# tool: binary_to_octal
# description: Takes a binary number and returns it in octal
# author: @Killerbrine06
# example: binary_to_octal "1010" -> "12"


def run(binary: str) -> str:
    return f"{int(binary, 2):o}"
