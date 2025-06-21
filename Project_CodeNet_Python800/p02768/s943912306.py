n,a,b=map(int,input().split())
def comb(n,k):
    nCk = 1
    MOD = 10**9+7

    for i in range(n-k+1, n+1):
        nCk *= i
        nCk %= MOD

    for i in range(1,k+1):
        nCk *= pow(i,MOD-2,MOD)
        nCk %= MOD
    return nCk

x=pow(2,n,10**9+7)-1
y=comb(n,a)+comb(n,b)
ans=x-y





while ans<0:
          ans+=10**9+7
print(ans)




