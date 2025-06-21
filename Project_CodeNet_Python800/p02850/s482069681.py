n = int(input())
ab = []
g = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
    ab.append([a,b])

k = max([len(i) for i in g])
print(k)

reach = [False]*n
c = dict()
from collections import deque
q = deque([[0,-1]])

while q:
    cur,col = q.popleft()
    reach[cur] = True
    for next_i in g[cur]:
        if not reach[next_i]:
            col = (col+1)%k
            a,b = sorted([cur,next_i])
            c[(a,b)] = col
            q.append([next_i,col])

for a,b in ab:
    print(c[(a,b)]+1)
