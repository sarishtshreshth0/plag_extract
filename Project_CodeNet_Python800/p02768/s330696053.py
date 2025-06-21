n, a, b = map(int, input().split())

MOD = 10**9 + 7

def comb(n, r, mod):
    if r > n-r:
        r = n - r
    
    res_X = 1
    for i in range(n-r+1, n+1):
        res_X = (res_X * i)%mod
    
    res_Y = 1
    for i in range(1, r+1):
        res_Y = (res_Y * i)%mod
    
    return (res_X * pow(res_Y, mod-2, mod))%mod

base = (pow(2, n, MOD) - 1)%MOD
a = comb(n, a, MOD)
b = comb(n, b, MOD)

print((base - a - b)%MOD)