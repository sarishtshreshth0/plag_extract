from collections import defaultdict
import heapq
N,M = map(int,input().split())
D = defaultdict(list)
for i in range(N):
    A,B = map(int,input().split())
    A = M - A
    D[A].append(B)

h = []

su = 0
hlen = 0
for i in range(M-1,-1,-1):
    for b in D[i]:
        heapq.heappush(h,-b)
        hlen += 1
    if hlen:
        su -= heapq.heappop(h)
        hlen -= 1

print(su)