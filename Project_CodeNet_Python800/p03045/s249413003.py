import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    x, y, z = map(int, input().split())
    x, y = x-1, y-1
    g[x].append(y)
    g[y].append(x)

s = []
visit = [-1]*n
cnt = 0
for i in range(n):
    if visit[i] == -1:
        s.append(i)
        cnt += 1
        visit[i] = cnt
        while s:
            v = s.pop()
            for u in g[v]:
                if visit[u] == -1:
                    visit[u] = visit[v]
                    s.append(u)
print(max(visit))