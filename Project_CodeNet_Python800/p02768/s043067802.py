
N, A, B = map(int, input().split())

MAX = 2 * 10 ** 5 + 1
MOD = 10 ** 9 + 7

# Factorial
fac = [0] * (MAX + 1)
fac[0] = 1
fac[1] = 1

# Inverse
inv = [0] * (MAX + 1)
inv[1] = 1

# Inverse factorial
finv = [0] * (MAX + 1)
finv[0] = 1
finv[1] = 1

for i in range(2, MAX + 1):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD

# Factorial for large
facl = [0] * (MAX + 1)
facl[0] = N
for i in range(1, MAX + 1):
    facl[i] = facl[i - 1] * (N - i) % MOD

# Solution
ans = pow(2, N, MOD) - 1
ans -= facl[A - 1] * finv[A] % MOD
ans %= MOD
ans -= facl[B - 1] * finv[B] % MOD
ans %= MOD
print(ans)
