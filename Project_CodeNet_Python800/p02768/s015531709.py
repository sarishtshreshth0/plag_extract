MOD = 10**9 + 7
n, a, b = map(int, input().split())

def comb(n, k):
    x, y = 1, 1
    for i in range(n, n-k, -1):
        x = x * i % MOD
    for i in range(1, k+1):
        y = y * i % MOD
    return x*pow(y, MOD-2, MOD) % MOD

ans = (pow(2, n, MOD)-1-comb(n,a)-comb(n,b)) % MOD

print(ans)