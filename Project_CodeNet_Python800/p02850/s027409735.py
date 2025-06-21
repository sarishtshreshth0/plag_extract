N = int(input())
data = [list(map(int,input().split())) for i in range(N-1)]

G = {}

for i in range(1,N+1):
    G[i] = []

for i in range(N-1):
    G[data[i][0]].append((data[i][1],i+1))
    G[data[i][1]].append((data[i][0],i+1))

M = max(len(G[i]) for i in range(1,N+1))

print(M)

from collections import deque

E = [0]+[-1]*(N-1)  #辺
E[1] = 1
q = deque([[data[0][0],1],[data[0][1],1]])

while q:
    n,i = q.pop()
    c = 1
    for dn,di in G[n]:
        if E[di] != -1:
            continue
        else:
            if c == E[i]:
                E[di] = M
                c += 1
                q.append([dn,di])
            else:
                E[di] = c
                c += 1
                q.append([dn,di])
for i in range(1,N):
    print(E[i])