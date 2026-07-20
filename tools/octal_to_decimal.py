# tool: octal_to_decimal
# description: converts an octal string to its decimal integer value
# author: @Solaris-star
# example: octal_to_decimal "77" -> "63"


def run(*args) -> str:
    try:
        return str(int(args[0], 8))
    except (ValueError, IndexError):
        bad = args[0] if args else ""
        return f"Error: '{bad}' is not a valid octal string"
