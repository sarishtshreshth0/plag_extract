import heapq
n,m = map(int,input().split())
B = [[] for _ in range(m)]
for i in range(n):
    a,b = map(int,input().split())
    if 1 <= a <= m:
        B[a-1].append(b)
task = []
heapq.heapify(task)
ans = 0
for i in range(m):
    for t in B[i]:
        heapq.heappush(task,-t)
    if task:
        ans += heapq.heappop(task)
print(-ans)
