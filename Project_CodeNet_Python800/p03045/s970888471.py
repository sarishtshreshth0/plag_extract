import sys
def input():
    return sys.stdin.readline()[:-1]
sys.setrecursionlimit(1000000)
n,m=map(int,input().split())
#xyz = [[]for i in range(m)]
g = [[]for i in range(n)]
for i in range(m):
    x,y,z = map(int,input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)

seen = [0 for i in range(n)]

def dfs(i):
    for nec in g[i]:
        if seen[nec]!=0:continue
        seen[nec]=1
        dfs(nec)

cnt = 0
for i in range(n):
    if seen[i] == 0:
        seen[i] = 1
        dfs(i)
        cnt+=1

print(cnt)
