import math

def nCr(n, r):
    return math.comb(n, r)

def nPr(n, r):
    return math.perm(n, r)

n = 5
r = 3

combination = nCr(n, r)
permutation = nPr(n, r)

print(f"nCr({n}, {r}) = {combination}")
print(f"nPr({n}, {r}) = {permutation}")
