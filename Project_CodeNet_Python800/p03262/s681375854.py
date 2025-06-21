import math
n,x=map(int,input().split());l=[abs(x-i) for i in list(map(int,input().split()))];r=0
for i in range(len(l)): r=math.gcd(r,l[i])
print(r)