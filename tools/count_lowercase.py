# tool: count_lowercase
# description: Count the number of lower case letters in a String
# author: @ShauryaPrakashVerma
# example: count_lowercase "Hello World" -> "8"


def run(*args) -> str:
    
    string = args[0]
    count = 0
    
    for char in string:
        if char.islower():
            count += 1
            
    return str(count)
