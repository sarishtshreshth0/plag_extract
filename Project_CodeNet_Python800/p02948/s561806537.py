import heapq
n, m = map(int, input().split())

jobs = [[] for i in range(10**5+1)]

for i in range(n):
    a, b = map(int, input().split())
    jobs[a].append(b)

candidate = []
ans = 0
for i in range(m+1):
    for j in jobs[i]:
        heapq.heappush(candidate, -j)

    # print(i, candidate)
    if len(candidate) >= 1:
        ans += heapq.heappop(candidate) * -1


print(ans)