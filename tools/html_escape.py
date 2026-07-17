# tool: html_escape
# description: Escapes HTML special characters
# author: @selvakanthanjagavan-byte
# example: html_escape "<div>" -> "&lt;div&gt;"

def run(*args) -> str:
    from html import escape

    text = args[0]
    return escape(text, quote=True)