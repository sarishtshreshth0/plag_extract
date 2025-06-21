from collections import deque
import sys

input = sys.stdin.buffer.readline
n = int(input())

graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append((b, i + 1))
    graph[b].append((a, i + 1))
par = [-1] * (n + 1)
que = deque([(1, -1, -1, -1)])  # edge, color, par, hen_num
color = [-1] * (n)
num = 0  # 使った色の数
while que:
    v, c, p, hen = que.popleft()
    par[v] = p
    color[hen] = c
    cnt = 0
    for i in range(len(graph[v])):
        u, hen_num = graph[v][i]
        if u == par[v]:
            continue
        cnt += 1
        if cnt == c:
            cnt += 1
        color[hen_num] = cnt
        num = max(num, cnt)
        que.append((u, cnt, v, hen_num))
print(num)
print(*color[1:], sep="\n")
