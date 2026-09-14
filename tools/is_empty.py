# tool: is_empty
# description: Check if a string is empty
# author: @Julito-Dev
# example: is_empty "" -> True

def run(*args) -> str:
    
    string = str(args[0])
    if string == "":
        return "True"

    else:
        return "False"