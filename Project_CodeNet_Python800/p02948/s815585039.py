from heapq import *
N,M=map(int,input().split())
X=[[] for i in range(M)]
A,B=0,0
for i in range(N):
  A,B=map(int,input().split())
  if A>M:
    continue
  X[-A].append(B)
P=0
Q=[]
heapify(Q)
for i in range(M-1,-1,-1):
  for j in range(len(X[i])):
    heappush(Q,-X[i][j])
  if len(Q):
    P-=heappop(Q)
print(P)