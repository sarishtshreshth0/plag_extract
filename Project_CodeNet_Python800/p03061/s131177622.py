from math import gcd
#================================================
N=int(input())
A=list(map(int,input().split()))

F=[0]*N
G=[0]*N

F[0]=A[0]
G[-1]=A[-1]

for i in range(1,N):
    F[i]=gcd(F[i-1],A[i])
    G[-(i+1)]=gcd(G[-i],A[-(i+1)])

F=[0]+F+[F[-1]]
G=[G[0]]+G+[0]

M=0
for i in range(N):
    M=max(M,gcd(F[i],G[i+2]))
print(M)
