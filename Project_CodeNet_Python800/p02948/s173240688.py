import heapq
N, M = map(int, input().split())
AB = [[] for _ in range(10**5+10)]
for _ in range(N):
	ta, tb = map(int, input().split())
	AB[ta].append(-tb)

ans = 0
q = []
for i in range(1,M+1):
	while AB[i]:
		heapq.heappush(q, AB[i].pop())

	if q:
		ans += heapq.heappop(q)

print(-ans)