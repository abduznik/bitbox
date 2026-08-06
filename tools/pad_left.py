# tool: pad_left
# description: Left-pad a string to a given width with a character
# author: @isaakchoi
# example: pad_left "42" "5" "0" -> "00042"

def run(*args) -> str:

    # NOTE - Returns full string if given width is less than or equal to the length of the string.
    
    import re
    
    if len(args) != 3:
        raise ValueError("Requires exactly three arguments: text, width, and padding character.")
    
    text = args[0]
    width = args[1]
    char = args[2]
    
    if not bool(re.fullmatch(r"\d+", width)):
        raise ValueError("Width must be a positive integer.")
    
    if len(char) != 1:
        raise ValueError("Padding character must be a single character.")
    
    return char * (int(width) - len(text)) + text
