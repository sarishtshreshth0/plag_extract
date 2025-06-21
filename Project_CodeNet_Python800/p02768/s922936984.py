import sys
input = sys.stdin.buffer.readline


def combination(k, r, MOD):
    """kCrを求める"""
    if k < r:
        return 0
    r = min(r, k - r)
    numer, denom = 1, 1
    for l in range(r):
        numer *= (k - l)
        numer %= MOD
        denom *= l + 1
        denom %= MOD
    return numer * pow(denom, MOD - 2, MOD) % MOD


n, a, b = map(int, input().split())
MOD = 10 ** 9 + 7


all_ptn = pow(2, n, MOD)
a_ptn = combination(n, a, MOD)
b_ptn = combination(n, b, MOD)

ans = (all_ptn - (a_ptn + b_ptn) - 1) % MOD
print(ans)