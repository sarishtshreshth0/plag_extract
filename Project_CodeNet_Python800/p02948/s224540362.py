import heapq
N, M = map(int,input().split())
L = [[] for _ in range(M)]
for _ in range(N):
    A, B = map(int,input().split())
    try:
        L[A-1].append(-B)
    except:
        pass
Q = []
ans = 0
for i in range(M):
    for j in L[i]:
        heapq.heappush(Q, j)
    try:
        ans -= heapq.heappop(Q)
    except:
        pass
print(ans)