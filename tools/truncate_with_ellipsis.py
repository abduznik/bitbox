# tool: truncate_with_ellipsis
# description: Truncate string and add ellipsis if shortened
# author: @isaakchoi
# example: truncate_with_ellipsis "hello world" "5" -> "hello..."

def run(*args) -> str:

    import math
    
    if len(args) != 2:
        raise ValueError("Requires exactly two arguments.")

    text = args[0]
    max_len = int(args[1])
    
    if max_len < 0:
        raise ValueError("Maximum length must be a non-negative integer.")
    
    if len(text) > max_len:
        return text[:max_len] + "..."

    return text
