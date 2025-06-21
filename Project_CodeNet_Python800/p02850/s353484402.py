#import numpy as np
from copy import deepcopy
import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
def pri(x): print('\n'.join(map(str, x)))

N = int(input())
#AB = [list(map(int, input().split())) for _ in range(N-1)]
edge = [[] for i in range(N)]
seen = [0]*N
colors = [0]*(N-1)
#for val in AB:
for i in range(N-1):
    x, y = list(map(int, input().split()))
    edge[x-1].append((i, y-1))
    edge[y-1].append((i, x-1))

lenedge = [len(val) for val in edge]
mledge = max(lenedge)
root = lenedge.index(mledge)
print(mledge)


que = deque()
que.append([(root, -1)])
while que[0]:
    nque = []
    cque = que.popleft()
    #print('cstack:', cstack)
    for tupl in cque:
        index, pcolor = tupl
        seen[index] = 1
        color = 1
        if (color == pcolor): color += 1
        for tupl2 in edge[index]:
            findex, edgei = tupl2
            if seen[edgei] == 0:
                nque.append((edgei, color))
                colors[findex] = color
                color += 1
                if (color == pcolor): color += 1
    que.append(nque)

#pri(color)

for color in colors:
    print(color)

