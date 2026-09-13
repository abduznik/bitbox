# tool: is_vowel
# description: Check if a character is a vowel or not
# author: @ShauryaPrakashVerma
# example: is_vowel "a" -> "True"


def run(*args) -> str:
    
    if len(args) < 1:
        return "Error: requires a string argument"
    
    string = args[0]
    
    if len(string) != 1:
        return "Error: Please enter a single character"
    
    vowels = "aeiouAEIOU"
    
    if string in vowels:
        return "True"
    else:
        return "False"
    
