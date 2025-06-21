import _heapq as heapq
n, m = [int(i) for i in input().split()]
ab = []
for _ in range(n):
    a, b = [int(i) for i in input().split()]
    ab.append([a, -b])
ab.sort()
j = 0
ans=0
h = []
for i in range(1, m + 1):
    while j<n and ab[j][0] <= i:
        heapq.heappush(h, ab[j][1])
        j += 1
    if h:
        ans += heapq.heappop(h)
print(-ans)
