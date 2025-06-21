import heapq
n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()
result, j = 0, 0
x = []
heapq.heapify(x)
for i in range(1, m+1):
    while j < n and ab[j][0] <= i:
        heapq.heappush(x, -ab[j][1])
        j += 1
    if len(x)!=0:
        result -= heapq.heappop(x)
print(result)