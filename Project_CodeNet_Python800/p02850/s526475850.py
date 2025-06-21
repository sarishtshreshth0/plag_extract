from collections import deque

n = int(input())
g = {i: set() for i in range(n)}
edge = []
for i in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    edge.append('{} {}'.format(a, b))
    g[a].add(b)
    g[b].add(a)

k = 0
ans = dict()
p_color = [0] * n
used = [1] + [0] * (n - 1)
que = deque([0])
while que:
    now = que.popleft()
    k = max(k, len(g[now]))
    color = 1
    for i in g[now]:
        if used[i]:
            continue
        if p_color[now] == color:
            color += 1
        p_color[i] = ans['{} {}'.format(now, i)] = ans['{} {}'.format(i, now)] = color
        color += 1
        used[i] = 1
        que.append(i)

print(k)
for e in edge:
    print(ans[e])
