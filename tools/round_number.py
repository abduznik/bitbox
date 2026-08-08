# tool: round_number
# description: Round a number to N decimal places
# author: @Solanki-Jatin
# example: round_number "3.14159" "2" -> "3.14"

def run(*args) -> str:
    n, places = args
    return str(round(float(n), int(places)))
