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

n,m=map(int,input().split())
x=list(map(int,input().split()))
x.sort()

if n>=m:
    print(0)
    quit()

ans=[]
for i in range(m-1):
    ans.append(x[i+1]-x[i])
# print(ans)

ans.sort()
# print(ans)
for i in range(n-1):
    ans[-1-i]=0
print(sum(ans))