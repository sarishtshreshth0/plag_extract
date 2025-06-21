import heapq

N, M = map(int, input().split())
jobs = {}
for _ in range(N):
    a, b = map(int, input().split())
    if a > M:
        continue
    if a not in jobs.keys():
        jobs[a] = []
    jobs[a].append(b)

ans = 0
canditates = []
for a in range(1, M+1):
    if a in jobs.keys():
        for b in jobs[a]:
            heapq.heappush(canditates, -b)
    else:
        if not canditates:
            continue
    ans += heapq.heappop(canditates) * (-1)

print(ans)