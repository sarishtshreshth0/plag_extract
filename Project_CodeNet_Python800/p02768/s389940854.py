from functools import reduce
def mycmb(n,r,p):
    r = min(r,n-r)
    if r == 0:
        return 1
    over = reduce(lambda x,y:x*y%p,range(n,n-r,-1))
    under = reduce(lambda x,y:x*y%p,range(1,r+1))
    return (over * pow(under,p-2,p))%p
    

n,a,b = map(int,input().split())
p = 10**9 + 7

syu = pow(2,n,p) - 1 - mycmb(n,a,p) - mycmb(n,b,p)
print(syu%p)