import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
N=int(input())

def dfs(u,par):
  col=1
  for v in graph[u]:
    if col==par:
      col+=1
    color_dic[(u,v)]=col
    dfs(v,col)
    col+=1

elist=[]
graph=[[] for _ in range(N+1)]
for _ in range(N-1):
  a,b=map(int,input().split())
  graph[a].append(b)
  elist.append((a,b))
#print(graph)

color_dic={}
dfs(1,-1)
#print(color_dic)

K=len(set(color_dic.values()))
print(K)
for e in elist:
  print(color_dic[e])