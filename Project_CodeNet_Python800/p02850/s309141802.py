from collections import deque

N = int(input())
X = [list(map(int, input().split())) for _ in range(N - 1)]

tree = [[] for _ in range(N + 1)]
for i, (a, b) in enumerate(X):
    tree[a].append((b, i))
    tree[b].append((a, i))

visited = [False] * (N + 1)
visited[1] = True
color = [0] * (N - 1)
stack = deque()
stack.append((1, 0))
while stack:
    u, c = stack.popleft()
    tmp = 0
    for v, i in tree[u]:
        if visited[v]:
            continue
            
        tmp += 1
        if tmp == c:
            tmp += 1
            
        visited[v] = True
        color[i] = tmp
        stack.append((v, tmp))

print(max(color))
print(*color, sep="\n")
