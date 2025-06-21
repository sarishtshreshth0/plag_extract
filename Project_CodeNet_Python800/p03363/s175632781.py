from collections import defaultdict
from itertools import accumulate
n=int(input())
a=[0]+list(accumulate(map(int,input().split()))) 
d=defaultdict(int)

for m in a:
  d[m]+=1
sm=0
for m in d.values():
  sm+=m*(m-1)//2
print(sm)
