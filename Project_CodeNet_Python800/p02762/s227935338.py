import sys
sys.setrecursionlimit(10**9)

n, m, k = map(int, input().split())
F = [[] for i in range(n)]
B = [[] for i in range(n)]
l = [0]*n

for i in range(m):
    a, b = map(int, input().split())
    F[a - 1].append(b - 1)
    F[b - 1].append(a - 1)

for i in range(k):
    c, d = map(int, input().split())
    B[c - 1].append(d - 1)
    B[d - 1].append(c - 1)

seen = [0]*n
cnt = 0
r = []

def dfs(x):
    if seen[x] == 0:
        r[cnt].add(x)
        seen[x] = 1
        for i in F[x]:
            dfs(i)

for i in range(n):
    if seen[i] == 0:
        r.append(set())
        dfs(i)
        cnt += 1

ans = [0]*n

for i in r:
    lr = len(i)
    for j in i:
        ans[j] = lr - len(F[j]) - len(i & set(B[j])) - 1

print(*ans)