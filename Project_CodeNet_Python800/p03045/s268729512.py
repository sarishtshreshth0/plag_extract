import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
from itertools import accumulate
from itertools import permutations
from itertools import combinations
from collections import defaultdict
from collections import Counter
import fractions
import math
from collections import deque
from bisect import bisect_left
from bisect import insort_left
import itertools
from heapq import heapify
from heapq import heappop
from heapq import heappush
import heapq
import numpy as np
INF = float("inf")
#d = defaultdict(int)
#d = defaultdict(list)
#N = int(input())
#A = list(map(int,input().split()))
#S = list(input())
#S.remove("\n")
#N,M = map(int,input().split())
#S,T = map(str,input().split())
#A = [int(input()) for _ in range(N)]
#S = [input() for _ in range(N)]
#A = [list(map(int,input().split())) for _ in range(N)]
N,M = map(int,input().split())
fr = [[] for _ in range(N)]
for _ in range(M):
    x,y,z = map(int,input().split())
    fr[x-1].append(y-1)
    fr[y-1].append(x-1)
used = [-1]*N #-1なら未探索。数字はrenketuのindex
renketu = []
index = 0
def dfs(fr,cur,parent,index,li):
    children = fr[cur]
    for chi in children:
        if chi == parent or used[chi] != -1:
            continue
        used[chi] = index
        li.append(chi)
        dfs(fr,chi,cur,index,li)
for i in range(N):
    if used[i] != -1:
        continue
    li = [i]
    used[i] = index
    dfs(fr,i,-1,index,li)
    index += 1
    renketu.append(li)
n = len(renketu)
print(n)