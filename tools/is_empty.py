# tool: is_empty
# description: Check if a String is empty
# author: @Julito-Dev
# example: is empty "" -> True

def run(*args) -> str:
    string = str(args[0])
    
    if string == "":
        return "True"
    else:
        return "False"
    