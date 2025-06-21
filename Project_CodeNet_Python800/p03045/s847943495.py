import sys, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from itertools import combinations, permutations, product
from heapq import heappush, heappop
from functools import lru_cache
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mat = lambda x, y, v: [[v]*y for _ in range(x)]
ten = lambda x, y, z, v: [mat(y, z, v) for _ in range(x)]
mod = 1000000007
sys.setrecursionlimit(1000000)

N, M = rl()
Q = []
for i in range(M):
	x, y, z = rl()
	x, y = x-1, y-1
	Q.append((x, y, z))

ids = [i for i in range(N)]
def find(x):
	if x != ids[x]:
		p = find(ids[x])
		ids[x] = p
	return ids[x]

def unite(x, y):
	x = find(x)
	y = find(y)
	ids[x] = y

for x, y, z in Q:
	unite(x,y)
for i in range(N):
	find(i)
print(len(Counter(ids)))
