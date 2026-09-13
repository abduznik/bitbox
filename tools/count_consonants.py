# tool: count_consonants
# description: Count the number of consonants in a String
# author: @ShauryaPrakashVerma
# example: count_consonants "Hello World" -> "7"


def run(*args) -> str:
    
    vowels = "aeiouAEIOU"
    
    if len(args) < 1:
        return "Error: requires a string argument"
    
    string = args[0]
    count = 0
    
    for char in string:
        if char.isalpha() and char not in vowels:
            count += 1
            
    return str(count)
