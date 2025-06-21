import sys
from heapq import heapify, heappop, heappush
import bisect

N, M = map(int, input().split())
AB = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])
A = [x for x, y in AB]

hq = []
heapify(hq)

count = 0

for i in range(1, M + 1):
    c_1 = bisect.bisect_left(A, i)
    c_2 = bisect.bisect_right(A, i)
    if c_2 - c_1 != 0:
        for j in range(c_1, c_2):
            heappush(hq, -AB[j][1])
    
    if hq:
        count += -heappop(hq)
    
print(count)