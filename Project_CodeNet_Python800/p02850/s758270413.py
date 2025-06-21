import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

ab = []
adj = [[] * (n+1) for _ in range(n+1)]

for i in range(n-1):
    a, b = list(map(int, input().split()))
    ab.append([a, b])
    adj[a].append(b)
    adj[b].append(a)

m = [0] * (n+1)
for a, b in ab:
    m[a] += 1
    m[b] += 1

k = max(m)
print(k)

visited = [False] * (n+1)
label = [(0, 0)] * (n+1)

j = m.index(k)

q = deque([j])
visited[j] = True
while len(q) > 0:
    v = q.popleft()
    l = 0
    for w in adj[v]:
        if not visited[w]:
            l += 1
            if label[v][1] == l:
                l += 1
            label[w] = (v, l)
            visited[w] = True
            q.append(w)

#print(adj)

for a, b in ab:
    if label[a][0] == b:
        print(label[a][1])
    else:
        print(label[b][1])