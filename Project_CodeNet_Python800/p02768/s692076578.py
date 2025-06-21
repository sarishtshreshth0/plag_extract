n,a,b=map(int,input().split())

def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

def mod_comb_count(n, r, mod):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res

mod=10**9+7
print((2*mod+(pow(2,n,mod)-1)-mod_comb_count(n,a,mod)-mod_comb_count(n,b,mod))%mod)
