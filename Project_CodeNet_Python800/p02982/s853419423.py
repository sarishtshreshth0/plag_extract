n,d=map(int, input().split())
x=[]
for i in range(n):
    tmp=[int(x) for x in input().split()]
    x.append(tmp)

import math

def dist(x,y):
    tmp=0
    for i in range(d):
        tmp+=(x[i]-y[i])**2
    return math.sqrt(tmp)

ans=0
import itertools
for seq in itertools.combinations(range(n),2):
    if dist(x[seq[0]],x[seq[1]]).is_integer():
        ans+=1
print(ans)