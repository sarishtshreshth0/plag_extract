import heapq
n, m = map(int, input().split())
albeits = [[] for _ in range(m+1)]
for i in range(n):
    a, b = map(int, input().split())
    if a <= m:
        albeits[a].append(b)

ans = 0
queue = []
heapq.heapify(queue)
# (M-1)日後から逆算して考える
for i in range(1, m+1):
    for item in albeits[i]:
        heapq.heappush(queue, -item)
    try:
        ans += -heapq.heappop(queue)
    except:
        pass

print(ans)
