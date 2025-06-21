from scipy.sparse.csgraph import dijkstra
import numpy as np
n=int(input())
graph=np.zeros((2*n+2,2*n+2),dtype=np.int64)
start,goal=0,2*n+1
l=[[int(j)for j in input().split()]for i in range(n)]
for i in range(1,1+n):
    c,d=map(int,input().split())
    for j,(a,b) in enumerate(l,n+1):
        if a<c and b<d:
            graph[start,i]=1
            graph[i,j]=1
            graph[j,goal]=1
def max_flow(graph):
    flow=0
    while True:
        dist,pred=dijkstra(graph,indices=start,return_predecessors=True,unweighted=True)
        if dist[goal]==np.inf:
            return flow
        path=[]
        v=goal
        while True:
            path.append((pred[v],v))
            v=pred[v]
            if v==start:
                break
        add_flow=min(graph[x][y] for x,y in path)
        for x,y in path:
            graph[x][y]-=add_flow
            graph[y][x]+=add_flow
        flow+=add_flow
print(max_flow(graph))