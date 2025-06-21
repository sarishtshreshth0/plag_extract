from math import *
N = int(input())
A = list(map(int,input().split()))
L = (N+1)*[0]
R = (N+1)*[0]
ans = []

for n in range(N):
  L[n]=gcd(L[n-1],A[n])

for n in range(N-1,0,-1):
  R[n]=gcd(R[n+1],A[n])

for n in range(N):
  ans+=[gcd(L[n-1],R[n+1])]

print(max(ans))