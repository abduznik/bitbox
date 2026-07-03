# tool: camel_to_snake
# description: converts a camelCase string to snake_case
# author: @shivsdev2
# example: camel_to_snake "helloWorld" -> "hello_world"

def run(*args) -> str:
    if not args:
        return ""
        
    text = str(args[0])
    snake_case = []
    
    for i, char in enumerate(text):
        if char.isupper() and i > 0:
            snake_case.append('_')
        snake_case.append(char.lower())
        
    return "".join(snake_case)