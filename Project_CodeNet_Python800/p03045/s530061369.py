import sys
sys.setrecursionlimit(10**7)

def dfs(G,v):
    seen[v] = True 
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G,next_v)
            
N,M = map(int,input().split())
G = [[]  for _ in range(N)]
seen= [False] * N 
cnt = 0

for i in range(M):
    x,y,z = map(int,input().split())
    G[x-1].append(y-1)
    G[y-1].append(x-1)
    
for v in range(N):
    if seen[v]:
        continue
    dfs(G,v)
    cnt += 1
    
print(cnt)    
