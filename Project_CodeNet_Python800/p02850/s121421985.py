from collections import deque

def bfs(s):
    q = deque()
    q.append([s, 0])
    while q:
        x, y = q.popleft()
        for g in G[x]:
            if color[g[1]] == -1:
                color[g[1]] = y + 1
                y += 1
                y %= k
                q.append([g[0], y])
    return

n = int(input())
G = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append([b, i])
    G[b].append([a, i])
k = 0
for g in G:
    k = max(k, len(g))
color = [-1] * (n - 1)
bfs(0)
print(k)
for i in color:
    print(i)