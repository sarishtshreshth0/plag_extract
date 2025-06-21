import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
G = [[] for _ in range(N)] # 辺の相手を保存
for i in range(N-1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append([b, i])
    G[b].append([a, i])

stack = deque([[0, 0]])
visited = [0] * N
visited[0] = 1
ans = [0] * (N-1)
while stack:
    i, pc = stack.pop()
    c = 1
    for ni, ln in G[i]:
        if not visited[ni]:
            visited[ni] = 1
            if c == pc:
                c += 1
            ans[ln] = c
            c += 1
            stack.append([ni, ans[ln]])

print(max(ans)) 
for c in ans:
    print(c)
