from collections import deque
N = int(input())
edges=[[] for _ in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    edges[a].append((b, i))
    edges[b].append((a, i))

next_set = deque([(0,0)])
colors = [0]*(N-1)
while next_set:
    p, i = next_set.popleft()
    cnt = 1 if colors[i] != 1 else 2
    for q, j in edges[p]:
        if colors[j] != 0:
            continue
        colors[j] = cnt
        cnt += 1
        if cnt == colors[i]:
            cnt += 1
        next_set.append((q, j))
print(max(colors))
print(*colors, sep="\n")
