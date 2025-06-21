from functools import reduce
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

n, a, b = map(int, read().split())
MOD = 10 ** 9 + 7


def comb_mod(n, a):
    num = reduce(lambda x, y: x * y % MOD, range(n, n - a, -1))
    den = reduce(lambda x, y: x * y % MOD, range(1, a + 1))
    return num * pow(den, MOD - 2, MOD) % MOD


ans = pow(2, n, MOD) - comb_mod(n, a) - comb_mod(n, b) - 1
ans %= MOD

print(ans)
