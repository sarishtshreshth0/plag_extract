import functools
import operator

n, a, b = map(int, input().split())

def nCr(n, r):
    r = min(r, n-r)
    if r == 0:
        return 1
    num = functools.reduce(lambda x, y: x*y%mod, range(n, n-r, -1))
    den = functools.reduce(lambda x, y: x*y%mod, map(lambda x: pow(x, mod-2, mod), range(1, r+1)))
    return num * den % mod

mod = 10**9 + 7
print((pow(2, n, mod) - nCr(n, a) - nCr(n, b) - 1) % mod)
