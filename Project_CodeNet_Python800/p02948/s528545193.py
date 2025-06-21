import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from collections import defaultdict
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
d = defaultdict(list)
for _ in range(N):
    a,b = map(int,input().split())
    d[a].append(b)
Q = [] 
heapify(Q)
s = 0
for i in range(1,M+1):
    li = d[i]
    for k in li:
        heappush(Q,-k)
    if len(Q) == 0:
        continue
    c = heappop(Q)
    s += -c
print(s)