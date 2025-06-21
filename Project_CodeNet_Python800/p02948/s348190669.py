from sys import stdin, stdout
input = stdin.readline
print = stdout.write

import heapq as hq
pq = []
hq.heapify(pq)
n, m = map(int, input().split())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
arr = sorted(arr, key=lambda x: x[0])
i = 0
ans = 0
for d in range(1, m + 1):
    while i < n and arr[i][0] <= d:
        hq.heappush(pq, -arr[i][1])
        i += 1
    if pq:
        ans -= hq.heappop(pq)
print(str(ans))
