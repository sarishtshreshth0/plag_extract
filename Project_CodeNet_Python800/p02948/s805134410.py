"""
Aの値が大きいものからheapqにぶち込んでいけばよい。
"""
from heapq import heappop,heappush
N,M = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
AB.sort(reverse=True)
que = []
for a,b in AB:
    if M >= a:
        heappush(que,b)
        M -= 1
    elif que:
        if que[0] < b:
            heappop(que)
            heappush(que,b)
print(sum(que))

