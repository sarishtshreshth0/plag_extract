from collections import defaultdict, deque

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n - 1)]

adj = [[] for _ in range(n + 1)]
for a, b in ab:
    adj[a].append(b)
    adj[b].append(a)

col_max = max([len(row) for row in adj])

cols = defaultdict(int)
s = 1
dq = deque([s])
p = [-1] * (n + 1)
p[s] = -2
while dq:
    u = dq.popleft()
    c_banned = cols[(u, p[u])]
    c = 1
    for v in adj[u]:
        if p[v] != -1:
            continue
        p[v] = u
        if c == c_banned:
            c += 1

        cols[(u, v)] = cols[(v, u)] = c
        c += 1

        dq.append(v)

print(col_max)
for a, b in ab:
    print(cols[(a, b)])
