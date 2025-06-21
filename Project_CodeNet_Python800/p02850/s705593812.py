import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


N = int(readline())
graph = [[] for _ in range(N+1)]
AB = []

for _ in range(N-1):
    a, b = map(int, readline().split())
    AB.append((a, b))
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N+1)
root = 1
stack = [root]
color = [0] * (N+1)
while stack:
    x = stack.pop()
    ng = color[x]
    c = 1
    for y in graph[x]:
        if y == parent[x]:
            continue
        if c == ng:
            c += 1
        parent[y] = x
        color[y] = c
        c += 1
        stack.append(y)

print(max(color))

for a, b in AB:
    if parent[a] == b:
        print(color[a])
    else:
        print(color[b])