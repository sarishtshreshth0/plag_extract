from collections import*
n=input()
a=list(map(int,input().split()))
d=dict(Counter(a))
mod=998244353
ans=a[0]==0 and d[0]==1
for i in d:
  if i==0:continue
  ans*=pow(d.get(i-1,0),d[i],mod)
  ans%=mod
print(ans)