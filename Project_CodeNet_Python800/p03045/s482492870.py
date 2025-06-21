import sys
sys.setrecursionlimit(10**6)

def f(j):
  nodes[j]=1
  for k in links[j]:
    if nodes[k]==0:
      f(k)

N, M=map(int, input().split())
XYZ=[list(map(int, input().split())) for _ in range(M)]
links=[[] for _ in range(N+1)]
for i in range(M):
  links[XYZ[i][0]].append(XYZ[i][1])
  links[XYZ[i][1]].append(XYZ[i][0])
  
nodes=[0]*(N+1)
ans=0
for i in range(1, N+1):
  if nodes[i]==0:
    ans+=1
    nodes[i]=1
    for j in links[i]:
      f(j)
      
print(ans)