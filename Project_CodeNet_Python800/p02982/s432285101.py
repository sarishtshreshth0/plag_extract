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
mod = 1000000007
sys.setrecursionlimit(1000000)

N, D = rl()
X = []
for i in range(N):
	X.append(rl())

def check(x, y):
	d = 0
	for i in range(D):
		d += (x[i]-y[i])**2
	d = d**0.5
	if d == int(d):
		return True
	return False

ans = 0
for i in range(N):
	for j in range(i+1, N):
		if check(X[i], X[j]):
			ans += 1
print(ans)