
MOD = 10 ** 9 + 7


def comb(n, k):
    if n < k or k < 0:
        return 0

    res = 1
    for i in range(1, k + 1):
        res = res * (n - i + 1) % MOD
        res = res * pow(i, MOD - 2, MOD) % MOD
    return res


N, A, B = map(int, input().split())
x1 = comb(N, A)
x2 = comb(N, B)
print((pow(2, N, MOD) - 1 - x1 - x2) % MOD)
