import heapq
N, M = map(int, input().split())
jobs = [[] for _ in range(M)]
for _ in range(N):
    A, B = map(int, input().split())
    if A > M:
        continue
    jobs[M-A].append(B)
ans = 0
q = []
heapq.heapify(q)
for i in range(M-1, -1, -1):
    for item in jobs[i]:
        heapq.heappush(q, item * (-1))
    if q:
        ans += heapq.heappop(q) * (-1)
print(ans)