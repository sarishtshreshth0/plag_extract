import sys
import collections
def input():
    return sys.stdin.readline()[:-1]
sys.setrecursionlimit(10000000)
n,m,k=map(int,input().split())
gf = [[]for i in range(n)]
gb = [[]for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    gf[a-1].append(b-1)
    gf[b-1].append(a-1)

for i in range(k):
    a,b = map(int,input().split())
    gb[a-1].append(b-1)
    gb[b-1].append(a-1)

seen = [0 for i in range(n)]

def dfs(i,k):
    for nec in gf[i]:
        if seen[nec]!=0:
            continue
        seen[nec]=k
        dfs(nec,k)
k=1

for i in range(n):
    if seen[i]==0:
        seen[i]=k
        dfs(i,k)
        k+=1
c = collections.Counter(seen)
lis = []
for i in range(n):
    dec = 0
    for k in gb[i]:
        if seen[i]==seen[k]:
            dec += 1
    lis.append(c[seen[i]]-len(gf[i])-dec-1)
print(*lis)
