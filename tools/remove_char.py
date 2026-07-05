# tool: remove_char
# description: Removes all occurrences of a character from a string
# author: @Dhruv-Kapri
# example: remove_char "hello" "l" -> "heo"


def run(*args) -> str:
    if len(args) == 1:
        return str(args[0])

    if len(args) != 2:
        return "Error: Expected 1 or 2 arguments."

    text = str(args[0])
    char = str(args[1])

    if len(char) != 1:
        return "Error: Second argument must be exactly one character."
        
    return text.replace(char, "")
