# tool: strip_html
# description: Removes all HTML tags from a string
# author: @its-Sohan
# example: strip_html "<p>Hello <b>world</b></p>" -> "Hello world"


import re


def run(*args) -> str:
    text = args[0]
    return re.sub(r"<[^>]+>", "", text)
