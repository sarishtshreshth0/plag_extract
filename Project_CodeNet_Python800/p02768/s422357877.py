from functools import reduce

n,a,b=map(int,input().split())

mod=10**9+7
def nCk(n,k):
    if n<k or (n<0 or k<0):
        return 0
    k=min(k,n-k)
    up,down=1,1
    for i in range(k):
        up=up*(n-i)%mod
        down=down*(i+1)%mod
    return up*pow(down,mod-2,mod)%mod

all=pow(2,n,mod)
nCa=nCk(n,a)
nCb=nCk(n,b)

print((all-nCa-nCb-1)%mod)