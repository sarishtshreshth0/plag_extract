n = int(input())
V = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    V[a].append([b,i])
    V[b].append([a,i])
m = 0
for W in V:
    m = max(m, len(W))
from collections import deque
q = deque([])
reach = [-1]*(n+1)
q.append([1,0])
reach[1] = 0
color = [0]*(n-1)
while q:
    x,c = q.popleft()
    j = 1
    for W,i in V[x]:
        if c == j:
            j += 1
        if reach[W] == -1:
            reach[W] = 0
            q.append([W, j])
            color[i] = j
            j += 1
print(m)
for i in range(n-1):
    print(color[i])