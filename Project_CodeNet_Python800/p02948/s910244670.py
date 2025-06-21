n,m = map(int,input().split())
ab = [[] for _ in range(10**5)]
for i in range(n):
	a,b = map(int,input().split())
	a -= 1
	ab[a].append(b)

import heapq

q = []
heapq.heapify(q)

ans = 0
for i in range(m):
	if len(ab[i]) != 0:
		for j in range(len(ab[i])):
			heapq.heappush(q,-1*ab[i][j])
	if len(q) != 0:
		ans += -1 * heapq.heappop(q)

print(ans)
