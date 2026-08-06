# tool: is_numeric
# description: Check if a string contains only digits
# author: @isaakchoi
# example: is_numeric "12345" -> "True"

def run(*args) -> str:

    import re
    
    if len(args) != 1:
        raise ValueError("Requires exactly one argument: text.")

    return str(bool(re.fullmatch(r"\d+", args[0])))
