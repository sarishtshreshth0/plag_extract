import bisect
import copy
import heapq
import math
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
sys.setrecursionlimit(500000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n=int(input())
d=deque([3,5,7])
# print(d)

ans=0
# dic={}
while d:
    tmp=d.popleft()
    if tmp<=n:
        s=Counter(str(tmp))
        if s["3"] and s["5"] and s["7"]:
            # print(tmp)
            ans+=1
        d.append(tmp*10+3)
        d.append(tmp*10+5)
        d.append(tmp*10+7)

print(ans)