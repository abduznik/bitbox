"""
# tool
# description: Converts an octal string to its decimal integer value
# author: Selvakanthan Jagavan
# example: octal_to_decimal "77" -> "63"
"""

def run(octal: str) -> str:
    return str(int(octal, 8))