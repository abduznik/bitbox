# tool: round_number
# description: Round a number to N decimal places
# author: @Solanki-Jatin
# example: round_number "3.14159" "2" -> "3.14"

def run(*args) -> str:
    if len(args) != 2:
        return "Error: Please provide exactly two arguments."
    try:
        n = float(args[0])
    except ValueError:
        return "Error: First argument must be a number."
    try:
        places = int(args[1])
    except ValueError:
        return "Error: Second argument must be an integer."
    return str(round(n, places))