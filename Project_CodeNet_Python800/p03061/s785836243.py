import math

N=int(input())
A=list(map(int,input().split()))
L=[0]*(N+1)
for i in range(N):
  L[i+1]=math.gcd(L[i],A[i])
R=[0]*(N+1)
for i in range(N-1,-1,-1):
  R[i]=math.gcd(R[i+1],A[i])
M=[]
for i in range(N):
  M.append(math.gcd(L[i],R[i+1]))
print(max(M))
