n,a,b=map(int,input().split())
mod=10**9+7

#modあり
def pow_speed(x,n):
    res = 1
    while n > 0:
        if n & 1 == 1:
            res *= x
        x *= x
        x%=mod
        n >>= 1
    return res

#nCx(mod)
def comb_speed(n,x):
    rec=1
    for i in range(n-x+1,n+1):
        rec=rec*i%mod
    rec2=1
    for i in range(1,x+1):
        rec2=rec2*i%mod
    rec2=pow_speed(rec2,mod-2)
    return (rec*rec2)%mod

print((pow_speed(2,n)-comb_speed(n,a)-comb_speed(n,b)-1)%mod)