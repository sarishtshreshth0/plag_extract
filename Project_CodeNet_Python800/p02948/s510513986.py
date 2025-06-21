import heapq
n, m = map(int, input().split())
M = [[] for _ in range(m + 1)]
q = []
for i in range(n):
    a, b = map(int, input().split())
    if a <= m:
        M[m - a] += [b]
for day in range(m + 1):
    for value in M[day]:
        if len(q) <= day:
            heapq.heappush(q, value)
        else:
            heapq.heappushpop(q, value)
print(sum(q))