# tool: is_empty_or_whitespace
# description: Checks if the input text is empty or contains only whitespace
# author: @isaakchoi
# example: is_empty_or_whitespace "   " -> "True"

def run(*args) -> str:
    
    if len(args) != 1:
        raise ValueError("Requires exactly one argument.")

    return str(args[0].strip() == "")
