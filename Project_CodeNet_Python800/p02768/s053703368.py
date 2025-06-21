n,a,b = map(int,input().split())
p = pow(10,9)+7

from functools import reduce
def comb(n,k,p):
    A = reduce(lambda x,y:x*y%p ,[n-k+1+i for i in range(k)])
    B = reduce(lambda x,y:x*y%p ,[i+1 for i in range(k)])
    return A*pow(B,p-2,p)%p

print((pow(2,n,p)-comb(n,a,p)-comb(n,b,p)-1)%p)