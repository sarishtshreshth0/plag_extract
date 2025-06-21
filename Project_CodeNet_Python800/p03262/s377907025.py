from math import gcd
n,x=map(int,input().split())
c=list(map(int,input().split()))
o=[]
if len(c)==1:
  print(abs(c[0]-x))
else:
  for i in c:
    o.append(abs(i-x))
  ans=gcd(o[1],o[0])
  for j in range(n-2):
      ans=gcd(ans,o[j+2])
  print(ans)