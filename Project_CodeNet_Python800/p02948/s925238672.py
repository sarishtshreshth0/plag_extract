N,M = list(map(int,input().split()))
X = [[]*3 for i in range(M)]
for i in range(N):
    A,B = list(map(int,input().split()))
    if A>M:
        continue
    else:
        X[M-A].append(B)

import heapq
out = 0
Y = []
heapq.heapify(Y)
for i in range(M):
    P = M-1-i
    Ls = X[P]
    for L in Ls:
        heapq.heappush(Y, -1*L)
    if len(Y)>0:
        Q = heapq.heappop(Y)
        out += -1*Q
print(out)