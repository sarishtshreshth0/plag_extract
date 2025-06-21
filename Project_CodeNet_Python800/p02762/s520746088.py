from collections import Counter
import sys

n, m, k = map(int, input().split())
F = [[] for _ in range(n)]
B = [[0] for _ in range(n)]

sys.setrecursionlimit(10**9)

for _ in range(m):
    a, b = map(int, input().split())
    F[a-1].append(b)
    F[b-1].append(a)

rks = [0]*(n)

def dfs(s,r):
    if rks[s] == 0:
        rks[s] = r
    for i in F[s]:
        if rks[i-1] != 0:
            continue
        dfs(i-1,r)

r = 0
for i in range(n):
    if rks[i] == 0:
        r += 1
        dfs(i,r)

for _ in range(k):
    c, d = map(int, input().split())
    if rks[c-1] == rks[d-1]:
        B[c-1][0] += 1
        B[d-1][0] += 1

counter = Counter(rks)
for i in range(n):
    print(counter[rks[i]] - len(F[i]) - (B[i][0]) - 1)


