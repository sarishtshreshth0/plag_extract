n = int(input())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append((b - 1, i))
    graph[b - 1].append((a - 1, i))
ans = [0] * (n - 1)

from collections import deque

d = deque()
d.append([0, -1])
while d:
    point, prev = d.popleft()
    color = 1 if prev != 1 else 2
    for a, index in graph[point]:
        if ans[index] == 0:
            ans[index] = color
            d.append([a, color])
            color += 1 if prev != color + 1 else 2
print(max(ans))
print(*ans, sep='\n')