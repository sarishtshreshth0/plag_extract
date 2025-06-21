n = int(input())
ab = [list(map(int, input().split())) for _ in range(n - 1)]

from collections import defaultdict
g = defaultdict(list)
for a, b in ab:
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

k = 0
for key in g:
    k = max(k, len(g[key]))
print(k)

ans = dict()
q = [(0, -1)] # (pos, used_color)
visited = set([0])
while q:
    cur, col = q.pop()

    if col == 0:
        tmp = 1
    else:
        tmp = 0

    for target in g[cur]:
        if target not in visited:
            q.append((target, tmp))
            visited.add(target)
            ans[(cur, target)] = tmp

            if tmp + 1 == col:
                tmp += 2
            else:
                tmp += 1

for a, b in ab:
    key = (a-1, b-1)
    print(ans[key] + 1)
