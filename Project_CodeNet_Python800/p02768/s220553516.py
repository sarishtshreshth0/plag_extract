mod=10**9+7
n,a,b = map(int,input().split())
def combination(n, r,mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * pow(i+1, mod-2, mod) % mod
    return res

N = pow(2,n,mod)-1
A = combination(n,a)
B = combination(n,b)
print((N-A-B)%mod)