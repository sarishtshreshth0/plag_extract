from collections import deque

n = int(input())
edge = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    edge[a-1].append([b-1, i])
    edge[b-1].append([a-1, i])

l = [len(i) for i in edge]
k = max(l)
root = l.index(k)

d = deque()
d.append([root, 0])
res = [0] * (n - 1)
while d:
    node, par_color = d.popleft()
    color = 0
    for e, idx in edge[node]:
        if res[idx] > 0:
            continue

        color += 1
        if color == par_color:
            color += 1
        d.append([e, color])
        res[idx] = color

print(k)
for c in res:
    print(c)