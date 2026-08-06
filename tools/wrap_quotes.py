# tool: wrap_quotes
# description: Wrap a string in single or double quotes
# author: @isaakchoi
# example: wrap_quotes hello double -> "hello"

def run(*args) -> str:
    
    if len(args) != 2:
        raise ValueError("Requires exactly two arguments: text and quote type.")

    text = args[0]
    quote_type = args[1].upper()
    
    if quote_type == "SINGLE":
        return f"'{text}'"
    elif quote_type == "DOUBLE":
        return f'"{text}"'
    else:
        raise ValueError("Quote type must be either 'single' or 'double'.")
