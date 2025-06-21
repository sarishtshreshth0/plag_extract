import collections
N=int(input())
D=list(map(int,input().split()))
mod=998244353
if D[0]!=0:
  print(0);exit()

D=collections.Counter(D)
if D[0]!=1:
  print(0);exit()
ans=1
for i in range(1,len(D)): 
  ans*=pow(D[i-1],D[i],mod)
  ans%=mod
print(ans)