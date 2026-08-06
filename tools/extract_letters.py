# tool: extract_letters
# description: Extract only letters from a string
# author: @isaakchoi
# example: extract_letters "a1b2c3" -> "abc"

def run(*args) -> str:

    # NOTE - Only a-z and A-Z are considered letters. All other characters are ignored.
    
    if len(args) != 1:
        raise ValueError("Requires exactly one argument")

    text = args[0]

    return "".join(filter(str.isalpha, text))
