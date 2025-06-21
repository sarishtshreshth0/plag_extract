import heapq

N, M = list(map(int,input().split()))
A = []
for i in range(N):
    in1, in2 = list(map(int,input().split()))
    A.append([in1, in2])

A = sorted(A)
ans = 0
day = 1
cnt = 0
x = []

for i in range(M):
    while(cnt < N):
        if A[cnt][0] == day:
            heapq.heappush(x, -A[cnt][1])
            cnt += 1
        else:
            break
    if x:  ans -= heapq.heappop(x)
    day += 1

print(ans)