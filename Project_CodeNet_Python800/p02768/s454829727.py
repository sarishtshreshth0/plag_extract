n, a, b = map(int, input().split())
MOD = 10**9+7

def comb(n, k, MOD):
    x = 1
    for i in range(k):
        x *= (n-i)
        x *= pow(i+1, MOD-2, MOD)
        x %= MOD
    return x

ans = pow(2, n, MOD) - 1 - comb(n, a, MOD) - comb(n, b, MOD)
ans += MOD
ans %= MOD
print(ans)