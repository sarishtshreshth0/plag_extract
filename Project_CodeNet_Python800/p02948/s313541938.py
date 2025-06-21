from heapq import heappush, heappop

n, m = map(int, input().split())
jobs = [[] for _ in range(10 ** 5 + 100)]
# 隣接リストっぽく
for i in range(n):
    a, b = map(int, input().split())
    jobs[a].append(b)

hq = []
res, j = 0, 0
for i in range(1, m + 1):
    for v in jobs[i]:
        heappush(hq, -v)
    if len(hq) > 0:
        res += -heappop(hq)
print(res)