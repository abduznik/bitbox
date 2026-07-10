# tool: html_escape
def run(*args) -> str:
    from html import escape

    text = args[0]
    return escape(text, quote=True)