from collections import deque

n = int(input())
g = [[] for _ in range(n)]
ab = []
for _ in range(n-1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append(b)
    g[b].append(a)
    ab.append((a, b))

q = deque([0])

chk = [False] * n
chk[0] = True

res = [0] * n
par = [0] * n
while q:
    x = q.popleft()
    cnt = 1
    for y in g[x]:
        if chk[y]:
            continue
        if res[x] == cnt:
            cnt += 1
        res[y], par[y], chk[y] = cnt, x, True
        cnt += 1
        q.append(y)

ans = []
for a, b in ab:
    if par[a] == b:
        ans.append(res[a])
    else:
        ans.append(res[b])

print(max(ans), *ans, sep="\n")
