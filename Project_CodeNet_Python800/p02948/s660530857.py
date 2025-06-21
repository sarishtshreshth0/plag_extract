import heapq
N, M = map(int, input().split())
S = list()
A = [list() for _ in range(M+1)]
for _ in range(N):
    a, b = map(int, input().split())
    if M < a:
        continue
    heapq.heappush(A[a], -b)

ans = 0
for i in range(1, M+1):
    for num in A[i]:
        heapq.heappush(S, num)
    if S == []:
        continue
    ans -= heapq.heappop(S)
print(ans)
