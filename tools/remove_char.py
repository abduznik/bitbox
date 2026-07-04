# tool: remove_char
# description: Removes all occurrences of a character from a string
# author: @Dhruv-Kapri
# example: remove_char "hello" "l" -> "heo"


def run(*args) -> str:
    text = args[0]
    char = args[1]
    return text.replace(char, "")
