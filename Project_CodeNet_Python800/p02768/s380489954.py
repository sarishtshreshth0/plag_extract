n,a,b = list(map(int, input().split()))
MOD = 10**9 + 7

from functools import lru_cache

MOD = 10**9+7
fact = [1]
fact_inv = [1]
fact_rev = [1]

for i in range(1, max(a,b)+1):
    fact.append(fact[i-1] * i % MOD)
    fact_inv.append(pow(fact[i], MOD-2, MOD))
    fact_rev.append(fact_rev[i-1] * (n-i+1) % MOD)

@lru_cache(maxsize=None)
def combi(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fact_rev[n] * fact_inv[k] % MOD

pattern = pow(2, n, MOD) - 1 
if a==b:
    pattern -= (combi(a, a))
else:
    pattern -= (combi(a, a) + combi(b, b))

print(pattern%MOD)