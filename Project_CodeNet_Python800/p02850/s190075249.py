from collections import Counter
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
edge = [[] for _ in range(N + 1)]
for i in range(N - 1):
    x, y = map(int, input().split())
    edge[x].append((y, i))
    edge[y].append((x, i))

color = [-1] * (N - 1)


def dfs(s, p=-1, pc=-1):
    c = 0
    for t, x in edge[s]:
        if color[x] != -1:
            continue
        if t == p:
            continue
        c += 1
        if c == pc:
            c += 1
        color[x] = c
        dfs(t, s, c)


dfs(1)

print(len(Counter(color)))
print(*color, sep="\n")