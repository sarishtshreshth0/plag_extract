from collections import deque
n = int(input())

graph = [[] for _ in range(n)]
edges = {}
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    # graph[b].append(a)
    edges[(a, b)] = i
    # edges[(b, a)] = i

que = deque([0])
ans = [0] * (n - 1)
visited = [-1] * n
visited[0] = 0
while que:
    a = que.popleft()
    c = 1
    for b in graph[a]:
        if visited[b] < 0:
            if visited[a] == c:
                c += 1
            visited[b] = c
            ans[edges[(a, b)]] = c
            c += 1
            que.append(b)

k = max(ans)
print(k)
for i in ans:
    print(i)


