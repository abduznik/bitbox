# tool: is_port
# description: Check if a number is a valid port number (0-65535)
# author: @Almond922
# example: is_port "8080" → "True"

def run(*args) -> str:
    try:
        port = int(args[0])
        return str(0 <= port <= 65535)
    except (ValueError, IndexError):
        return "False"
