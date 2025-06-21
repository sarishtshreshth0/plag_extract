import collections
n=int(input())
A=list(map(int,input().split()))
if A[0]!=0:
  print(0)
  exit()
mod=998244353
C=[0]*n
for i in range(n):
  C[A[i]]+=1
ans=1
if C[0]!=1:
  print(0)
  exit()
for i in range(n-1):
  ans=ans*pow(C[i],C[i+1],mod)%mod
print(ans)