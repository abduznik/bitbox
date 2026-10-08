# tool: sort_chars
# description: Sort characters in a string
# author: bongurishi
# example: sort_chars("c b a") -> "  abc"

def run(*args) -> str:
    if len(args) != 1:
        return "Error: Please provide exactly one argument."

    return "".join(sorted(args[0]))
    