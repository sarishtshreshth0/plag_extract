n,a,b = map(int, input().split())
mod = 10**9 + 7

def modcmb(n,r,mod):
    x,y = 1,1
    for i in range(1, r + 1):
        x *= (n - i + 1)
        x %= mod
        y *= i
        y %= mod
    rtn = x * pow(y, mod - 2, mod) % mod
    return rtn

ans = pow(2, n, mod) - 1
ans -= modcmb(n,a,mod) + modcmb(n,b,mod)
print(ans % mod)
