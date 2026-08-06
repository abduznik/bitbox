# tool: trim
# description: Remove leading and trailing whitespace
# author: @isaakchoi
# example: trim "  hello  " -> "hello"

def run(*args) -> str:
    
    if len(args) != 1:
        raise ValueError("Requires exactly one argument: text.")

    text = args[0]
    
    return text.strip()
