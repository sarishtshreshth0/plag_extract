from heapq import heapify, heappop, heappush
N,M = map(int, input().split())
AB = []
for i in range(N):
    a,b = map(int, input().split())
    AB.append((a,-b))
AB.sort()

Q = []
ans = 0
i = 0

for day in range(M):
    while i<N and AB[i][0] == day+1:
        heappush(Q, AB[i][1])
        i+=1
    if Q:
        ans -= heappop(Q)
print(ans)