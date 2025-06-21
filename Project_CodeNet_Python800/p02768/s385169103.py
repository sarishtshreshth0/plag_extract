MOD = 10**9 + 7

def modpow(a: int, p: int, mod: int) -> int:
    # return a**p (mod MOD) O(log p)
    res = 1
    while p > 0:
        if p & 1 > 0:
            res = res * a % mod
        a = a**2 % mod
        p >>= 1
    return res

def comb(N, x):
    numerator = 1
    for i in range(N-x+1, N+1):
        numerator = numerator * i % MOD
    denominator = 1
    for j in range(1, x+1):
        denominator = denominator * j % MOD
    d = modpow(denominator, MOD-2, MOD)
    return numerator * d
    
n,a,b=map(int,input().split())

ans = (modpow(2,n,MOD)-1 - comb(n,a) - comb(n,b)) % MOD
print(ans)