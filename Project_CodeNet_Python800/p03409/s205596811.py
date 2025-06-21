# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

N=int(input())
edge=[[] for _ in range(N*2+2)]
a,b=[0]*N,[0]*N
for i in range(N):
    a[i],b[i]=map(int,input().split())
for i in range(N):
    c,d=map(int,input().split())
    for j in range(N):
        if c>a[j] and d>b[j]:
            edge[i].append([j+N,1,len(edge[j+N])])
            edge[j+N].append([i,0,len(edge[i])-1])
for i in range(N):
    edge[N*2].append([i,1,len(edge[i])])
    edge[i].append([N*2,0,len(edge[N*2])-1])
    edge[N*2+1].append([i+N,0,len(edge[i+N])])
    edge[i+N].append([N*2+1,1,len(edge[N*2+1])-1])

def dfs(v,t,f):
    if v==t:
        return f
    used[v]=True
    for i,(nv,cap,rev) in enumerate(edge[v]):
        if not used[nv] and cap>0:
            d=dfs(nv,t,min(f,cap))
            if d>0:
                edge[v][i][1]-=d
                edge[nv][rev][1]+=d
                return d
    return 0

flow=0
while True:
    used=[False]*(N*2+2)
    f=dfs(N*2,N*2+1,INF)
    if f==0:
        break
    flow+=f
print(flow)