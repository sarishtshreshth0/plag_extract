from math import gcd
n=int(input())
a=list(map(int,input().split()))

l=[0]*n
r=[0]*n

for i in range(n-1):
  l[i+1]=gcd(l[i],a[i])
for i in range(n-1,0,-1):
  r[i-1]=gcd(r[i],a[i])
ans=0
for i in range(n):
  ans=max(ans,gcd(l[i],r[i]))
print(ans)