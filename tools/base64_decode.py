# tool: base64_decode
# description: Decodes a Base64 string back to plain text
# author: @rdhadge
# example: base64_decode "aGVsbG8=" -> "hello"

import base64

def run(*args) -> str:
    text = args[0]
    decoded_str = base64.b64decode(text)
    return decoded_str.decode('utf-8')