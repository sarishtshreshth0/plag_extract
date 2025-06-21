n,a,b = map(int,input().split())
modnum = 10**9+7
ans = pow(2,n,modnum)-1

def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)
def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res
ans -= combination(n, a, modnum)
ans -= combination(n, b, modnum)
ans %= modnum
print(ans)