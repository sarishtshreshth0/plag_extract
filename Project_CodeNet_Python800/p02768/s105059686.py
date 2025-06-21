from functools import reduce
def comb(n, r, mod=10 ** 9 + 7):
    numerator = reduce(lambda x, y: x * y % mod, [n - r + k + 1 for k in range(r)])
    denominator = reduce(lambda x, y: x * y % mod, [k + 1 for k in range(r)])
    return numerator * pow(denominator, mod - 2, mod) % mod

n, a, b = map(int, input().split())
mod = 1000000007
print((pow(2, n, mod) - 1 - comb(n, a, mod) - comb(n, b, mod)) % mod)
