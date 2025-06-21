import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
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
N = int(input())
ab = [list(map(int,input().split())) for _ in range(N-1)]
tree = [[] for _ in range(N)]
for i in range(N-1):
    a,b = ab[i]
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
    index = -1
    MAX = 0
for i in range(N):
    li = tree[i]
    n = len(li)
    if n > MAX:
        MAX = n
        index = i
d = defaultdict(int)

def dfs(cur,parent,prevcolor):
    li = tree[cur]
    n = len(li)
    if n == 0:
        return
    flag = 0
    for i in range(n):
        chi = li[i]
        if chi == parent:
            flag = 1
            continue
        a = (prevcolor+1+i)%MAX
        if flag == 1:
            a -= 1
        d[(cur,chi)] = a
        d[(chi,cur)] = a
        dfs(chi,cur,a)
dfs(index,-1,0)
print(MAX)
for i in range(N-1):
    a,b = ab[i]
    ans = d[(a-1,b-1)]
    if ans == 0:
        ans += MAX
    print(1+ans%MAX)