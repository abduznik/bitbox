# tool: meters_to_feet
# description: Converts meters to feet
# author: @cgkol2005
# example: meters_to_feet 1 -> 3.28084

def run(*args) -> str:
    """Convert meters to feet."""
    if not args:
        return "Error: No input provided"
    
    try:
        meters_val = float(args[0])
        feet_val = meters_val * 3.28084
        return str(round(feet_val, 5))
    except ValueError as e:
        return f"Invalid input for meters: {e}"
