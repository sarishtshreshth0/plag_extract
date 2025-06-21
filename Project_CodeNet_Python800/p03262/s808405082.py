import math
n,s=map(int,input().split())
X=list(map(int,input().split()))
for i in range(n):
  X[i]=abs(X[i]-s)
X.sort()
ans=10**100
for x in X:
  tmp=math.gcd(X[0],x)
  if tmp<ans:
    ans=tmp
print(ans)