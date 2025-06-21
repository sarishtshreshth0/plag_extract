from math import gcd
N=int(input())
A=list(map(int,input().split()))
L=[0]
R=[0]
for i in range(N):
  L.append(gcd(L[i],A[i]))
  R.append(gcd(R[i],A[-i-1]))
R=R[::-1]
P=0
for i in range(N):
  P=max(P,gcd(L[i],R[i+1]))
print(P)