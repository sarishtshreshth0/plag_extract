from collections import *
from itertools import *

N=int(input())
A=list(map(int,input().split()))

s1=[0]+list(accumulate(A))
nums=defaultdict(int)
for i in range(N+1):
  nums[s1[i]]+=1

ans=0
s2=set(s1)
for x in s2:
  ans+=nums[x]*(nums[x]-1)//2

print(ans)
