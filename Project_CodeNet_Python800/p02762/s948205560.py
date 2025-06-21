from collections import deque
N,M,K = map(int,input().split())
G = {i:[] for i in range(1,N+1)}
for _ in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
col = [-1 for _ in range(N+1)]
cnt = 0
for i in range(1,N+1):
    if col[i]<0:
        col[i] = cnt
        que = deque([i])
        while que:
            x = que.popleft()
            for y in G[x]:
                if col[y]<0:
                    col[y] = cnt
                    que.append(y)
        cnt += 1
C = {}
for i in range(1,N+1):
    c = col[i]
    if c not in C:
        C[c] = 0
    C[c] += 1
B = {i:[] for i in range(1,N+1)}
for _ in range(K):
    c,d = map(int,input().split())
    B[c].append(d)
    B[d].append(c)
A = []
for i in range(1,N+1):
    c = col[i]
    cnt = C[c]-len(G[i])-1
    for y in B[i]:
        if col[y]==c:
            cnt -= 1
    A.append(cnt)
print(*A)