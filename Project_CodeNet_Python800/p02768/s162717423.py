n, a, b = map(int, input().split())
mod = 10**9+7

ans = pow(2, n, mod)-1

def choose(n, r):
    res = 1
    fac = 1
    for i in range(r):
        res *= n-i
        res %= mod
        fac *= i+1
        fac %= mod
    return res*pow(fac, mod-2, mod)%mod

ans -= choose(n, a)
ans -= choose(n, b)

print(ans%mod)