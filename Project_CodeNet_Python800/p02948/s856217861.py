import heapq
from collections import deque
N,M = map(int,input().split())
A = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x:x[0])
A = [(-A[i][1],A[i][0]) for i in range(N)]
A = deque(A)
heap = []
cnt = 0
for i in range(M-1,-1,-1):
    k = M-i
    while len(A)>0 and A[0][1]<=k:
        heapq.heappush(heap,A.popleft())
    if len(heap)>0:
        b,a = heapq.heappop(heap)
        b = -b
        cnt += b
print(cnt)