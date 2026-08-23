# tool: is_alpha
# description: Check if a string contains only letters
# author: @Almond922
# example: is_alpha "hello" → "True"

def run(*args) -> str:
    try:
        text = args[0]
        return str(text.isalpha())
    except IndexError:
        return "False"
