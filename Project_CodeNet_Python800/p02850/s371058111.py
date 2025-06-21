from collections import deque, defaultdict
n = int(input())
l = [[] for i in range(n + 1)]
ab = [list(map(int, input().split())) for i in range(n - 1)]
for a, b in ab:
    l[a].append(b)
    l[b].append(a)
que = deque([1])
p = [-1] * (n + 1)
p[1] = -2
ma = max([len(i) for i in l])
d = defaultdict(int)
print(ma)
while que:
    u = que.popleft()
    x = d[(u, p[u])]
    c = 1
    for v in l[u]:
        if p[v] != -1:
            continue
        p[v] = u
        if c == x:
            c += 1
        d[(u, v)] = d[(v, u)] = c
        c += 1
        que.append(v)
for a, b in ab:
    print(d[(a, b)])