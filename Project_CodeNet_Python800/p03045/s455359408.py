import queue
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
XYZ = []
for _ in range(M):
    XYZ.append(tuple(map(int, input().split())))

G=[[] for _ in range(N+1)]
for el in XYZ:
    G[el[0]].append(el[1])
    G[el[1]].append(el[0])
#print(G)

seen=[False]*(N+1)
todo=queue.Queue()
def bfs(n):
    seen[n]=True
    for nxt in G[n]:
        if seen[nxt]==False:
            bfs(nxt)


cnt=0
for check in range(1, N+1):
    if seen[check]==False:
        cnt+=1
        bfs(check)
print(cnt)
