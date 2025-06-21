from collections import deque
def color_available(unavailable, K):
    idx = 0
    L = len(unavailable)
    unavailable = sorted(unavailable)
    for color in range(K):
        if idx < L and color == unavailable[idx]:
            idx += 1
        else:
            yield color

def bfs(graph, N, K, start):
    colors = [dict() for _ in range(N)]
    visited = [0] * N
    visited[start] = 1
    que = deque([start])
    while que:
        node = que.popleft()
        gen = color_available(colors[node].values(), K)
        for n in graph[node]:
            if not visited[n]:
                visited[n] = 1
                colors[node][n] = colors[n][node] = next(gen)
                que.append(n)
    return colors

N = int(input())
graph = [[] for _ in range(N)]
inputs = tuple(tuple(map(lambda n: int(n) - 1, input().split())) for _ in range(N - 1))
counts = [0] * N
for i, j in inputs:
    graph[i].append(j)
    graph[j].append(i)
    counts[i] += 1
    counts[j] += 1
K = max(counts)
colors = bfs(graph, N, K, 0)
print(K)
for i, j in inputs:
    print(colors[i][j] + 1)