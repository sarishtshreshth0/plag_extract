import sys
n=int(input())
ans=[0]*(n+1)
MOD=998244353
a=list(map(int,input().split()))
if a[0]!=0:
  print(0)
  sys.exit()
for i in range(n):
  ans[a[i]]+=1
if ans[0]!=1:
  print(0)
  sys.exit()
fin=1
for i in range(1,max(a)+1):
  fin=(fin*pow(ans[i-1],ans[i],MOD))%MOD
print(fin)