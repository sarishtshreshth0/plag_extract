import math
n, a, b = map(int, input().split())
MOD = 1000000007

def cmb(n, r, MOD):
    x, y = 1, 1
    for i in range(r):
        x = x * (n - i) % MOD
        y = y * (i + 1) % MOD
    return x * pow(y, MOD - 2, MOD) % MOD

N = pow(2, n, MOD) - 1
A = cmb(n, a, MOD)
B = cmb(n, b, MOD)

print((N - A - B) % MOD)