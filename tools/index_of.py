# tool: index_of
# description: Find the index of first occurrence of a substring
# author: @mmaxjr
# example: index_of "hello" "ll" -> "2"

def run(*args) -> str:
    text = args[0]
    sub = args[1]
    return str(text.find(sub))
