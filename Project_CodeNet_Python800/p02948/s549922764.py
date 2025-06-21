import heapq
n, m = map(int, input().split())
a = sorted([list(map(int, input().split())) for _ in range(n)])
r,j,x=0,0,[]
heapq.heapify(x)
for i in range(m):
    while j < n and a[j][0] <= i+1:
        heapq.heappush(x, -a[j][1])
        j += 1
    if x:
        r -= heapq.heappop(x)
print(r)