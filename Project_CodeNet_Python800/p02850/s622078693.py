from collections import deque
n = int(input())
graph = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append((b-1, i))
    graph[b-1].append((a-1, i))

queue = deque([0])
seen = [False]*n
seen[0] = True
colors = [None]*n
ans = [None]*(n-1)
while len(queue)>0:
    node = queue.popleft()
    c = 1
    for c_node, edge in graph[node]:
        if seen[c_node]:
            continue
        if colors[node]==c:
            c += 1
        ans[edge] = c
        colors[c_node] = c
        seen[c_node] = True
        queue.append(c_node)
        c += 1
print(max(ans))
for i in ans:
    print(i)