# https://atcoder.jp/contests/abc146/tasks/abc146_d

n = int(input())

graph = [[] for _ in range(n)]
edges = {}
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
    edges[(a, b)] = i
    edges[(b, a)] = i

ans = [0] * (n - 1)
stack = [0]
visited = [-1] * n
visited[0] = 0
while stack:
    node = stack.pop()
    color = 1
    for p in graph[node]:
        if visited[p] < 0:
            if visited[node] == color:
                color += 1
            visited[p] = color
            t = edges[(p, node)]
            ans[t] = color
            stack.append(p)
            color += 1

print(max(ans))
for a in ans:
    print(a)
