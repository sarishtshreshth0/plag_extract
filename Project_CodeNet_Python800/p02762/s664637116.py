from collections import deque

def dfs(start):
    S = deque([start])
    link = {start}
    VL[start] = 1
    while S:
        node = S.pop()
        for f in AB[node]:
            if VL[f] == 1:
                continue
            link.add(f)
            S.append(f)
            VL[f] = 1
    for l in link:
        res[l] = len(link) - len(link & AB[l]) - len(link & CD[l]) - 1

N, M, K = map(int, input().split())

AB = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    AB[a].add(b)
    AB[b].add(a)

CD = [set() for _ in range(N)]
for _ in range(K):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    CD[c].add(d)
    CD[d].add(c)

VL = [0] * N
res = [0] * N

for i in range(N):
    if VL[i] == 0:
        dfs(i)

print(*res)
