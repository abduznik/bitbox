# tool: ini_get
# description: gets a value from INI-style text by section and key
# author: @Solaris-star
# example: ini_get "[a]\nx=1" "a" "x" -> "1"

import configparser
from io import StringIO


def run(*args) -> str:
    if len(args) < 3:
        return "Error: expected ini_text, section, key"
    text, section, key = args[0], args[1], args[2]
    parser = configparser.ConfigParser()
    try:
        parser.read_file(StringIO(text))
    except configparser.Error as exc:
        return f"Error: {exc}"
    if not parser.has_section(section):
        return f"Error: section '{section}' not found"
    if not parser.has_option(section, key):
        return f"Error: key '{key}' not found in section '{section}'"
    return parser.get(section, key)
