from functools import reduce

n, a, b = map(int, input().split())
mod = 10 ** 9 + 7

#combination高速化の裏技
def comb(N, A, MOD):
    num = reduce(lambda x, y: x * y % MOD, range(N, N - A, -1))
    den = reduce(lambda x, y: x * y % MOD, range(1, A + 1))
    return num * pow(den, MOD - 2, MOD) % MOD

#powはmodを引数にしてあまりを計算してくれる
print((pow(2, n, mod = mod) - 1 - comb(n, a, mod) - comb(n, b, mod)) % mod)