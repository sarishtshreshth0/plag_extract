import math
n,x=map(int,input().split());l=[abs(x-i) for i in list(map(int,input().split()))]
if len(l)>1:
  r=math.gcd(l[0],l[1])
  for i in range(1,len(l)):
    r=math.gcd(r,l[i])
else:
  print(l[0])
  exit()
print(r)