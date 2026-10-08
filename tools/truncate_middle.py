# tool: truncate_middle
# description: Truncates the given amount of characters from the middle of a string and appends "..."
# author: @marcosistoocommon
# example: truncate_middle "Hello World" "5" → "Hel...rld"
from math import floor

def run(*args) -> str:
    if len(args) < 2 or not isinstance(args[0], str):
        return "Error: Please enter a String and a Number"

    try:
        trunc = int(args[1])
    except (ValueError, TypeError):
        return "Error: Please enter a String and a Number"

    if trunc < 0:
        return "Error: The Number must be positive"
    text = args[0]
    if trunc == 0 and len(text)>0:
        return text
    if len(text) <= trunc:
        return "..."
    shift = (len(text)-trunc)/2
    left_shift =  floor(shift)
    if shift>left_shift:
        right_shift=left_shift+1
    else:
        right_shift=left_shift
    return text[:left_shift] + "..." + text[-right_shift:]
