# tool: permutation_count
# description: Calculates the number of permutations P(n, r) of selecting and ordering r items from a set of n items.
# author: @farukttbasar
# example: run("5", "3") -> "60"
def run(n: str, r: str) -> str:
    try:
        val_n = int(n)
        val_r = int(r)
    except (ValueError, TypeError):
        return "Error: Arguments must be valid integers"
        
    if val_n < 0 or val_r < 0:
        return "Error: Arguments must be non-negative integers"

    if val_r > val_n:
        return "Error: r cannot be greater than n"

    ans = 1
    for i in range(val_n, val_n - val_r, -1):
        ans *= i

    return str(ans)
