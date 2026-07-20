# tool: strip_html
# description: Removes HTML tags from a string
# author: @Solaris-star
# example: strip_html "<b>hi</b>" -> "hi"

import re

def run(*args) -> str:
    if len(args) != 1:
        return "Error: Expected exactly 1 argument."
    text = args[0]
    return re.sub(r"<[^>]+>", "", text)
