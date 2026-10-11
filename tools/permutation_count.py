# tool: permutation_count
# description: Calculates the number of permutations P(n, r) of selecting and ordering r items from a set of n items.
# author: @farukttbasar
# example: permutation_count(5, 3) returns "60"

def run(n: str, r: str) ->str:
    n, r= int(n), int(r)
    ans = 1
    for i in range(n, n-r, -1):
        ans *= i
    return str(ans)
