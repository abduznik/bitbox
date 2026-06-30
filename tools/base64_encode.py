# tool: base64_encode
# description: Encodes a string to Base64
# author: @rdhadge
# example: base64_encode "hello" -> "aGVsbG8="

import base64

def run(*args) -> str:
    text = args[0]
    encoded_str = base64.b64encode(text.encode('utf-8'))
    return encoded_str.decode('utf-8')