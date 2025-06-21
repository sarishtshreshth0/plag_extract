import math
n,x=map(int,input().split())
l=list(map(int,input().split()))
d=abs(l[0]-x)
for m in l:
  d2=math.gcd(d,abs(m-x))
  d=min(d,d2)
print(d)