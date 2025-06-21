MOD=10**9+7
def pow(x,n,mod):
    ans = 1
    while n>0:
        if n&1==1:
            ans*=x
            ans%=mod
        x = x*x
        x%=mod
        n = n>>1
    return ans

N,a,b=map(int,input().split())
xa=1
for i in range(N,N-a,-1):
  xa*=i
  xa%=MOD
xb=xa
for i in range(N-a,N-b,-1):
  xb*=i
  xb%=MOD
ya=1
for i in range(2,a+1):
  ya*=i
  ya%=MOD
yb=ya
for i in range(a+1,b+1):
  yb*=i
  yb%=MOD
ans=(pow(2,N,MOD)-1
     -(xa*pow(ya,MOD-2,MOD)%MOD)
     -(xb*pow(yb,MOD-2,MOD)%MOD))%MOD
print(ans)