import sys
from collections import deque
input = sys.stdin.readline

n, m, k = list(map(int, input().split()))

ab = [list(map(int, input().split())) for _ in range(m)]
cd = [list(map(int, input().split())) for _ in range(k)]

ff = [[] for _ in range(n+1)]
for a, b in ab:
    ff[a].append(b)
    ff[b].append(a)

visited = [False] * (n+1)
visited[0] = True

com = [-1] * (n+1)


def dfs(v, ff, visited, com, g):
    q = deque([v])
    visited[v] = True
    com[v] = g
    k = 1
    while len(q) > 0:
        w = q.pop()
        for x in ff[w]:
            if not visited[x]:
                q.append(x)
                visited[x] = True
                com[x] = g
                k += 1
    return k

g = 0
group_num = []

for i in range(1, n+1):
    if visited[i]:
        pass
    else:
        k = dfs(i, ff, visited, com, g)
        group_num.append(k)
        g += 1

#print(com)

friends = [0] * (n+1)

for i in range(1, n+1):
    friends[i] += group_num[com[i]] - 1

for a, b in ab:
    if com[a] == com[b]:
        friends[a] -= 1
        friends[b] -= 1

for c, d in cd:
    if com[c] == com[d]:
        friends[c] -= 1
        friends[d] -= 1

print(" ".join(map(str, friends[1:])))