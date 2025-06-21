import heapq

N,M = list(map(int,input().split()))
works = [list(map(int,input().split())) for i in range(N)]

works.sort()
day = 1
ans = 0
candidates = []
for work in works:
    if work[0] == day:
        heapq.heappush(candidates,-work[1])
    else:
        if M < work[0]:
            break
        while day < work[0]:
            if candidates:
                ans += -heapq.heappop(candidates)
            day += 1
        heapq.heappush(candidates,-work[1])

while day <= M:
    if candidates:
        ans += -heapq.heappop(candidates)
    day += 1

print(ans)