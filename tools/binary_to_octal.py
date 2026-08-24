# tool: binary_to_octal
# description: Takes a binary number and returns it in octal
# author: @Killerbrine06
# example: binary_to_octal "1010" -> "12"


def run(*args) -> str:
    try:
        binary = args[0]
    except IndexError:
        return "Error: Function must have argument"
    
    if type(binary) != str:
        return "Error: Argument must be of type str"
    
    try:
        octal = f"{int(binary, 2):o}"
        return octal
    except ValueError:
        return f"Error: '{binary}' is not a valid binary string"
    
if __name__ == "__main__":
    print(run("\102"))
