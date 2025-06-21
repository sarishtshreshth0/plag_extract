from collections import deque

N = int(input())
K = 0
Ans = [0] * (N-1)
Edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append((b, _))
    Edge[b].append((a, _))

Q = deque()
Q.append((0, 0))
P = [-1] * N
while Q:
    now, color = Q.popleft()
    cnt = 1
    for nex, num in Edge[now]:
        if cnt == color:
            cnt += 1
        if nex == P[now]:
            continue
        if Ans[num] != 0:
            continue
        Q.append((nex, cnt))
        Ans[num] = cnt
        K = max(cnt, K)
        cnt += 1

print(K)
for a in Ans:
    print(a)