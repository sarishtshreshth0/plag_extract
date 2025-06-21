from math import*
N,x=map(int,input().split())
*X,=map(int,input().split())
ans=abs(X[0]-x)
now=X[0]
for i in X[1:]:
    ans=gcd(ans,abs(i-now))
    now=i

print(ans)