# tool: is_uuid
# description: Checks whether a string is a valid UUID format
# author: @PurpleSwtr
# example: is_uuid "550e8400-e29b-41d4-a716-446655440000" -> "True"


import uuid


def run(*args) -> str:
    if not args:
        return "False"

    text = args[0]
    if not isinstance(text, str):
        return "False"

    try:
        uuid.UUID(text)
        return "True"
    except ValueError:
        return "False"
