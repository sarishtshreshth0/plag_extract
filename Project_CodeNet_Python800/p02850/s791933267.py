from queue import Queue
from sys import stdin, stdout
input = stdin.readline
print = stdout.write

n = int(input())
adj = [[] for _ in range(n + 1)]
edges = []
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
    edges.append((a, b))

root = 0
maxdeg = 0
for i in range(1, n + 1):
    if len(adj[i]) > maxdeg:
        maxdeg = len(adj[i])
        root = i

print(str(maxdeg) + '\n')
colors = [i+1 for i in range(maxdeg)]

hashc = {}
q = Queue()
q.put((root, -1, -1))
while not q.empty():
    u, par, col = q.get()
    i = 0
    for child in adj[u]:
        if child == par: continue
        if colors[i] == col: i += 1
        hashc[(u, child)] = colors[i]
        hashc[(child, u)] = colors[i]
        q.put((child, u, colors[i]))
        i += 1

for e in edges:
    print(str(hashc[e]) + '\n')
