from collections import deque
from collections import defaultdict

n = int(input())
graph = defaultdict(list)

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append([b, i])
    graph[b].append([a, i])

ans = [0] * (n - 1)

q = deque([[1, 0, 0]])
while q:
    v, pcol, root = q.popleft()
    cnt = 1
    for node in graph[v]:
        if node[0] == root:
            continue
        if cnt == pcol:
            cnt += 1
        ans[node[1]] = cnt
        q.append([node[0], cnt, v])
        cnt += 1

print(max(ans))
print(*ans, sep="\n")
