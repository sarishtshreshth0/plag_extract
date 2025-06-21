N, M = map(int, input().split())
AB = [[] for _ in range(10**5+1)]
for _ in range(N):
    a, b = map(int, input().split())
    AB[a].append(b)

import heapq
h = []
heapq.heapify(h)

ans = 0
for a in range(1,M+1):
    for b in AB[a]:
        heapq.heappush(h, -b)
    heapq.heappush(h, 0)
    ans -= heapq.heappop(h)
    
print(ans)