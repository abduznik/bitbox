# tool: snake_to_kebab
# description: Convert snake_case to kebab-case
# author: @ShauryaPrakashVerma
# example: snake_to_kebab "hello_world" -> "hello-world"

def run(*args) -> str:
    if len(args) < 1:
        return "Error: requires a string argument"

    text = args[0]
    return text.replace("_", "-")