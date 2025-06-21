import heapq


N, M = map(int, input().split())
Work = [tuple(map(int, input().split())) for _ in range(N)]

Work.sort()
now = 1
Q = []
ans = 0
for day, reward in Work:
    if day > M:
        break
    if now > M:
        break
    if day == now:
        heapq.heappush(Q, -reward)
    else:
        while day - now > 1:
            if len(Q) > 0:
                a = heapq.heappop(Q)
                ans += a
            now += 1
        if len(Q) > 0:
            a = heapq.heappop(Q)
            ans += a
        heapq.heappush(Q, -reward)
        now = day
while M - now >= 0:
    if len(Q) > 0:
        a = heapq.heappop(Q)
        ans += a
    now += 1

print(-ans)