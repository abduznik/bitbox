# tool: mime_from_ext
# description: Returns the MIME type for a file extension
# author: @Doomguy-BFG9000
# example: mime_from_ext ".png" -> "image/png"

import mimetypes


def run(*args) -> str:
    if len(args) != 1:
        return "Error: Requires exactly one argument"

    extension = str(args[0]).strip()
    if not extension:
        return "application/octet-stream"

    if not extension.startswith("."):
        extension = f".{extension}"

    mime_type, _ = mimetypes.guess_type(f"file{extension}", strict=False)
    return mime_type or "application/octet-stream"
