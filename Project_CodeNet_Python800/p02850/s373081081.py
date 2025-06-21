n = int(input())
g = [[] for _ in range(n)]
inv = [0] * n
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append((b - 1, i))
    inv[a - 1] += 1
    g[b - 1].append((a - 1, i))
    inv[b - 1] += 1
k = max(inv)
print(k)
s = [0]
d = [-1] * n
d[0] = [-2]
ans = [0] * (n - 1)
while s:
    p = s.pop()
    c = 1
    for node, idx in g[p]:
        if d[node] == -1:
            if c == d[p]:
                c += 1
            d[node] = c
            ans[idx] = c
            c += 1
            s.append(node)
for x in ans:
    print(x)
