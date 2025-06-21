def BFS(x):
  cnt=1
  v=deque([x])
  k=0
  zu[x]=k
  lis=[x]
  roots[x]=x
  
  while len(v)>0:
    a=v.popleft()
    roots[a]=x
    for i in fr[a]:
      if zu[i]==-1:
        zu[i]=zu[a]+1
        v.append(i)
        cnt += 1
        lis.append(i)

          
  return lis

##############################

from collections import deque
N,M,K=map(int,input().split())
A=[0]*M
B=[0]*M
C=[0]*K
D=[0]*K
fr=[ [] for _ in range(N)]
bl=[ set() for _ in range(N)]
zu=[ -1 for _ in range(N)] #訪問済みリスト
roots= [ -1 for _ in range(N)]

for i in range(M):
  A[i],B[i]= map(int,input().split())
  fr[A[i]-1].append(B[i]-1)
  fr[B[i]-1].append(A[i]-1)
for k in range(K):
  C[k],D[k]= map(int,input().split())
  bl[C[k]-1].add(D[k]-1)
  bl[D[k]-1].add(C[k]-1)
fr_set= [set(fr[i]) for i in range(N)]
    
size=[0]*N
pena=[0]*N
for i in range(N):
  if zu[i]==-1:
    kumi=BFS(i) #リスト
    for k in range(len(kumi)):
      size[kumi[k]]=len(kumi)
      
      
ans=[0 for _ in range(N)]      
for i in range(N):
  ans[i]= size[i]-1 - len(fr[i])
  for j in bl[i]:
    if roots[j]==roots[i]:
      ans[i] -= 1      
      
print(*ans)
