# tool: char_at
# description: Returns the character at a given index
# author: @GabrielTrifoni
# example: char_at "hello" 1 -> "e"

def run(*args) -> str:
    string = args[0]
    
    try:
        index = int(args[1])
    except ValueError:
        raise ValueError("Second argument must be an integer.")

    if index >= len(string):
        raise ValueError(f"Index is out of range for string.")

    return string[index]