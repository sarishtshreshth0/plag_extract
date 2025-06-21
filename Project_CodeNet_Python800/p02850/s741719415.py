N =int(input())

edge = [[] for i in range(N)]
adj = [[] for i in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append((b, i))
    adj[b].append((a, i))

K = 0
for i in range(N):
    K = max(K, len(adj[i]))
print(K)

from collections import deque
color = [-1] * (N - 1)
qu = deque([0])
done = [False] * N
done[0] = True
vc = [-1] * N
while(len(qu) > 0):
    v = qu.popleft()
    for nv, e in adj[v]:
        if not done[nv]:
            vc[v] = (vc[v] + 1) % K
            color[e] = vc[v]
            qu.append(nv)
            vc[nv] = vc[v]
            done[nv] = True

for i in range(N - 1):
    print(color[i] + 1)