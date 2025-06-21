from collections import *
from itertools import *

N=int(input())
A=list(map(int,input().split()))

s=[0]+list(accumulate(A))
s_cnt=Counter(s)

ans=0
for x in s_cnt.values():
  ans+=(x*(x-1))//2

print(ans)
