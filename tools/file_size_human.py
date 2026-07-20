# tool: file_size_human
# description: Formats a byte size as a human-readable string
# author: @Solaris-star
# example: file_size_human "1536" -> "1.5 KB"

def run(*args) -> str:
    if len(args) != 1:
        return "Error: Expected exactly 1 argument."
    try:
        size = float(args[0])
    except ValueError:
        return "Error: Size must be a number."
    if size < 0:
        return "Error: Size must be non-negative."
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    idx = 0
    while size >= 1024 and idx < len(units) - 1:
        size /= 1024
        idx += 1
    if idx == 0 or size.is_integer():
        return f"{int(size)} {units[idx]}"
    return f"{size:.1f} {units[idx]}"
