def combinations_count(n, r, mod):
    r = min(r, n-r)
    p,k = 1,1
    for i in range(1,r+1):
        p *= (n-i+1)
        k *= i
        p = p%mod
        k = k%mod
    return p*inv(k,mod)%mod
def inv(a, mod):
    return pow(a, mod - 2, mod)
def D():
    n,a,b = list(map(int, input().split()))
    mod = 10**9+7
    res = pow(2,n,mod) - 1
    res -= combinations_count(n, a, mod)
    res -= combinations_count(n, b, mod)
    print(res%mod)
D()