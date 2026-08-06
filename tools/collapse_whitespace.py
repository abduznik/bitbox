# tool: collapse_whitespace
# description: Collapses consecutive whitespace characters in the input text into a single space
# author: @isaakchoi
# example: collapse_whitespace "This   is   a   test." -> "This is a test."

def run(*args) -> str:
    
    if len(args) != 1:
        raise ValueError("Expected exactly one argument.")

    import re
    
    return re.sub(r'\s+', ' ', args[0])
