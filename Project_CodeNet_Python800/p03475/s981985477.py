import math
n=int(input())
c=[0]*(n-1)
s=[0]*(n-1)
f=[0]*(n-1)
for i in range(n-1):
  c[i],s[i],f[i] = map(int,input().split())

for i in range(n):
  ans=0
  for j in range(i,n-1):
    ans = max(s[j], math.ceil(ans/f[j])*f[j]) + c[j]
  print(ans)