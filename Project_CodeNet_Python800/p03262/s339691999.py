from functools import reduce
import math

n,x=map(int,input().split())
a=sorted(map(int,input().split()))
a=[i-x for i in a]

if len(a)==1:print(abs(a[0]));exit()
if len(a)==2:print(math.gcd(a[0],a[1]));exit()

l=[]
for y in range(n-1):
    l.append(a[y+1]-a[y])
    
print(reduce(lambda x,y:math.gcd(x,y),l))