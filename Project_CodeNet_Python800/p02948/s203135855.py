import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

import heapq
import collections

N, M = rl()
daytasks = collections.defaultdict(list)
for i in range(N):
	a, b = rl()
	daytasks[a].append(b)

heap = []
ans = 0
for i in range(1, M+1):
	for t in daytasks[i]:
		heapq.heappush(heap, (-t, i))
	if len(heap) > 0:
		b, a = heapq.heappop(heap)
		b = -b
		ans += b
print(ans)

