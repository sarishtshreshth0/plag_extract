from heapq import heapify, heappush, heappop
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ABs = [tuple(map(int, input().split())) for _ in range(N)]

ABs.sort()

PQ = []
iAB = 0
ans = 0
for rest in range(1, M+1):
    while iAB < N and ABs[iAB][0] <= rest:
        heappush(PQ, -ABs[iAB][1])
        iAB += 1
    if PQ:
        B = -heappop(PQ)
        ans += B

print(ans)
