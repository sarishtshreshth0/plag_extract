MOD = 10**9 + 7
n, a, b = map(int, input().split())

def C(n,r):
    p = n*pow(r,MOD-2,MOD)
    for i in range(1,r):
        p = p*(n-i)%MOD
        p = p * pow(i,MOD-2,MOD)
    return p%MOD



print((pow(2,n,MOD) - C(n,a) - C(n,b)-1)%MOD)