import heapq

n, m = map(int, input().split())
pay = sorted([[-int(i) for i in input().split()] for _ in range(n)])

res = 0
pq = []
for i in range(1, m+1):
    while pay and -pay[-1][0] <= i:
        a, b = pay.pop()
        heapq.heappush(pq, b)
    if pq:
        res -= heapq.heappop(pq)

print(res)
