N, M = [int(s) for s in input().split()]
rewards = list(filter(lambda x: x[0] <= M
                , sorted([[int(s) for s in input().split()] for _ in range(N)])))[::-1]

import heapq
a = []
heapq.heapify(a)

sums = 0
for day in reversed(range(M)):
    while(rewards):
        if M-day >= rewards[-1][0]:
            r = rewards.pop()
            heapq.heappush(a, -1 * r[1])
        else:
            break
    
    if a:
        sums += -1 * heapq.heappop(a)

print(sums)
