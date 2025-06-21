import heapq

n, m = map(int, input().split())
l = [[] for _ in range(m)]
 
for i in range(n):
    a, b = map(int, input().split())
    if a <= m:
        l[a - 1].append(b)

a = []
ans = 0

for k in range(m - 1, -1, -1):
    i = m - k - 1
    for j in l[i]:
        heapq.heappush(a, (-1) * j)
    if a:
        ans += heapq.heappop(a) * (-1)
        
print(ans)
