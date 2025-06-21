import math

n, a, b = map(int, input().split())
MOD = 1000000000 + 7

inv = [1, 1]
com = [0, n]
for i in range(2, max(a, b) + 1):
    inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
    com.append(com[i - 1] * (n - i + 1) * inv[i] % MOD)

print((pow(2, n, MOD) - com[a] - com[b] - 1) % MOD)
