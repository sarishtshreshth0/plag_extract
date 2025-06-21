import math
n,x=map(int,input().split())
a=list(map(int,input().split()))

g=0

for y in a:
  g=math.gcd(g,abs(y-x))
  
print(g)