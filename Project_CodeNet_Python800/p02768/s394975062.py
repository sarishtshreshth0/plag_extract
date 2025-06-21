n, a, b = map(int, input().split())

MOD = 10 ** 9 + 7

ans = pow(2, n, MOD) - 1
na = 1
for i in range(a):
    na *=(n - i)
    na %= MOD
    na *= pow(i + 1, MOD - 2, MOD)
    na %= MOD
ans -= na
nb = 1
for i in range(b):
    nb *= (n - i)
    nb %= MOD
    nb *= pow(i + 1, MOD - 2, MOD)
    nb %= MOD
ans -= nb
print(ans % MOD)