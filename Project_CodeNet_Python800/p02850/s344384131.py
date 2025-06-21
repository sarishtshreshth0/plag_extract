import sys
from collections import deque
read = sys.stdin.read

N, *ab = map(int, read().split())
graph = [[] for _ in range(N + 1)]

for a, b in zip(*[iter(ab)] * 2):
    graph[a].append(b)

color = [0] * (N + 1)
queue = deque([1])

while queue:
    V = queue.popleft()
    number = 1
    for v in graph[V]:
        if number == color[V]:
            number += 1
        color[v] = number
        queue.append(v)
        number += 1

print(max(color))
for a, b in zip(*[iter(ab)] * 2):
    print(color[b])
