N, M = map(int, input().split())

path = [[] for _ in range(N)]
for _ in range(M):
    x, y, _ = map(int, input().split())
    path[x-1].append(y-1)
    path[y-1].append(x-1)

seen = [False] * (N+1)

last_start = -1
counter = 0
while True:
    start = last_start + 1
    while seen[start]:
        start += 1

    if start == N:
        break

    if path[start]:
        stack = [start]
        while stack:
            pos = stack.pop()
            seen[pos] = True
            for next_node in path[pos]:
                if not seen[next_node]:
                    stack.append(next_node)
    else:
        seen[start] = True

    counter += 1
    last_start = start

print(counter)