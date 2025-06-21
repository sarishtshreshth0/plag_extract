from math import*
n=int(input())
a=list(map(int,input().split()))
b=[a[0]]
c=[a[-1]]
for i in range(1,n):
  b+=[gcd(b[-1],a[i])]
  c+=[gcd(c[-1],a[-i-1])]
ans=0
c=c[::-1]
for i in range(n):
  if i==0:ans=max(ans,c[i+1])
  elif i==n-1:ans=max(ans,b[i-1])
  else:
    ans=max(ans,gcd(c[i+1],b[i-1]))
print(ans)