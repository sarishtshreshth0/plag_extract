import heapq
N, M = map(int, input().split())
value = [[] for _ in range(10 ** 5 + 1)]

for _ in range(N):
    a, b = map(int, input().split())
    value[a].append(-1 * b)

koho = value[1]
heapq.heapify(koho)

ans = 0
for i in range(1, M + 1):
    if len(koho) > 0:
        ans += -1 * heapq.heappop(koho)
    if i < M:
        for v in value[i + 1]:
            heapq.heappush(koho, v)

print(ans)