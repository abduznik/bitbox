# tool: is_numeric
# description: Check if a string contains only digits
# author: @imnaur
# example: is_numeric "12345" -> "True"



def run(text: str) -> str:
    """Function checks if text is numeric and return True/False in str"""
    result = bool(text) and text.isdigit()
    return str(result)
