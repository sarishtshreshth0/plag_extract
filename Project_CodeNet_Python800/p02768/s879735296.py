N,A,B=map(int,input().split())
p=10**9+7
def cmb(n,k):
    x,y = 1,1
    for i in range(k):
        x=x*(n-i)%p
        y=y*(i+1)%p
    return x*pow(y,p-2,p)%p
print((pow(2,N,p)-cmb(N,A)-cmb(N,B)-1)%p)