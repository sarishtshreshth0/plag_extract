import sys
from collections import deque
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
g = [[] for _ in range(n)] #隣接リスト
ab = []
for i in range(n-1):
    a,b = map(int,readline().split())
    a,b = a-1,b-1
    ab.append((a,b))
    g[a].append(b)
    g[b].append(a)

root = 0
parent = [0]*n
deq = deque([root])
order = [root]

color = [-1]*n
deq = deque([root])
while deq:
    fr = deq.pop()
    ng = color[fr]
    c = 0
    for go in g[fr]:
        if go == parent[fr]:
            continue
        if c == ng:
            c += 1
        parent[go] = fr
        color[go] = c
        c += 1
        deq.append(go)
        order.append(go)
rank = [0]*n
for i,j in enumerate(order):
    rank[j] = i
print(max(color)+1)
for a,b in ab:
    if rank[a] < rank[b]:
        print(color[b]+1)
    else:
        print(color[a]+1)