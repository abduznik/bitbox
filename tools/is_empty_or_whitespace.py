# tool: is_empty_or_whitespace
# description: Check if a string is empty or contains only whitespace
# author: @imnaur
# example: is_empty_or_whitespace "   " -> "True"



def run(text: str) -> str:
    """Function checks if text empty or has only whitespaces and return True/False in str"""
    is_empty = not text or not text.strip()
    return str(is_empty)