from heapq import heappush, heappop

n, m = map(int, input().split())
arbeit = [[] for _ in range(m)]
for _ in range(n):
    a, b = map(int, input().split())
    if a > m:
        continue
    heappush(arbeit[a-1], -b)

ans = 0
next_vals = []
for i in range(m):
    if any(arbeit[i]):
        b = heappop(arbeit[i])
        heappush(next_vals, (b, i))
    if any(next_vals):
        b, i = heappop(next_vals)
        ans -= b
        if any(arbeit[i]):
            b = heappop(arbeit[i])
            heappush(next_vals, (b, i))
print(ans)