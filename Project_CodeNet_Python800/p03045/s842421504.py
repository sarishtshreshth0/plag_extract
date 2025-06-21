import sys
from collections import defaultdict,deque
input = sys.stdin.readline
N,M= map(int,input().split())
XYZ= [list(map(int,input().split())) for i in range(M)]
g = defaultdict(list)

for x,y,z in XYZ:
    g[x].append(y)
    g[y].append(x)

visited = [False] * (N+1)

connect = 0
for i in range(1,N+1):
    if visited[i]:
        continue
    connect += 1
    dq = deque([i])
    while dq:
        v = dq.pop()
        visited[v] = True
        for nv in g[v]:
            if visited[nv]:
                continue
            dq.append(nv)

print(connect)
        





