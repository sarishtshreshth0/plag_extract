# ABC156 D

n,a,b=map(int,input().split())
p=10**9+7



def nCr_init(L,p):
    for i in range(L+1):
        if i<=1:
            inv[i]=1
        else:
            inv[i]=(p-inv[p%i]*(p//i))%p


def pow_k(x,n,p=10**9+7):
    if n==0:
        return 1
    K=1
    while n>1:
        if n%2!=0:
            K=(K*x)%p
        x=(x*x)%p
        n//=2
    return (K*x)%p


nck=[0]*(b+10)
inv=[1]*(b+15)
nck[0]=1

nCr_init(b+10,p)
for i in range(b+5):
    nck[i+1]=(nck[i]*(n-i)*inv[i+1])%p

print((pow_k(2,n,p)-nck[a]-nck[b]-1)%p)