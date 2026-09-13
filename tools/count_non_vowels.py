# tool: count_non_vowels
# description: Count the number of non-vowels characters in a String
# author: @ShauryaPrakashVerma
# example: count_non_vowels "Hello World" -> "8"


def run(*args) -> str:
    
    if len(args) < 1:
        return "Error: requires a string argument"
    
    vowels = "aeiouAEIOU"
    
    string = args[0]
    count = 0
    
    for char in string:
        if char in vowels:
            continue
        else:
            count += 1
            
    return str(count)
