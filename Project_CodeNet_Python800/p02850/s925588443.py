import sys
 
n = int(input())
links = [set() for _ in range(n)]
for i, line in enumerate(sys.stdin):
    a, b = map(int, line.split())
    a -= 1
    b -= 1
    links[a].add((i, b))
    links[b].add((i, a))
 
ans = [-1] * (n - 1)
k = max(map(len, links))
q = [(0, -1)]
fixed = set()
 
while q:
    v, c = q.pop()
    color = 1
    if c == color:
        color += 1
    for i, u in links[v]:
        if ans[i] != -1:
            continue
        ans[i] = color
        q.append((u, color))
        color += 1
        if c == color:
            color += 1
 
print(k)
print('\n'.join(map(str, ans)))