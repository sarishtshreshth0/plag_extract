MOD = 10**9 + 7

N, A, B = map(int, input().split())

def getComb(n, k, MOD):
    if n < k:
        return 0
    if n-k < k:
        k = n-k
    comb = 1
    for x in range(n-k+1, n+1):
        comb = (comb * x) % MOD
    d = 1
    for x in range(1, k+1):
        d = (d * x) % MOD
    comb *= pow(d, MOD-2, MOD)
    return comb % MOD

ans = pow(2, N, MOD) - 1
ans -= getComb(N, A, MOD)
ans -= getComb(N, B, MOD)
ans %= MOD

print(ans)
