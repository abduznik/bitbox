# tool: generate_uuid
# description: Generates a random UUID v4 string
# author: @PurpleSwtr
# example: generate_uuid -> "3f6b2c1a-8e4d-4b7f-9c2a-1d5e8f3a6b0c"


import uuid


def run(*args) -> str:
    return str(uuid.uuid4())
