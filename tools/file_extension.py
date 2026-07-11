# tool: file_extension
# description: Extracts the file extension from a file path
# author: @tmshnko
# example: file_extension "photo.JPG" -> ".jpg"


def run(*args) -> str:
    txt = str(args[0])
    last_dot = txt.rfind('.') 
    last_slash = txt.rfind('/')

    if last_dot <= last_slash:
        return ""
    return txt[last_dot:].lower()
