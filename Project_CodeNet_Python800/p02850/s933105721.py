import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import deque

n = int(readline())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, readline().split())
    graph[a].append((b, i))
    graph[b].append((a, i))
color = [-1] * (n + 1)
color[1] = -2
ans = [0] * (n - 1)

def bfs(s):
    stack = deque([s])
    while stack:
        num = 1
        now = stack.pop()
        for next, idx in graph[now]:
            if color[next] != -1:
                continue
            if color[now] == num:
                num += 1
            color[next] = num
            ans[idx] = num
            num += 1
            stack.append(next)


bfs(1)
print(max(ans))
print('\n'.join(map(str, ans)))
