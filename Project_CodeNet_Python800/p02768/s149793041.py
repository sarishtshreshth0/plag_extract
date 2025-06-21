from functools import reduce
MOD = 10**9 + 7
n, a, b = map(int, input().split())

def comb(n, k):
    def mul(a, b):
        return a*b%MOD
    x = reduce(mul, range(n, n-k, -1))
    y = reduce(mul, range(1, k+1))
    return x*pow(y, MOD-2, MOD) % MOD

ans = (pow(2, n, MOD)-1-comb(n,a)-comb(n,b)) % MOD

print(ans)