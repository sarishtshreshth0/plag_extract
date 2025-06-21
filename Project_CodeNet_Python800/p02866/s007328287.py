from collections import defaultdict
n=int(input())
d=list(map(int,input().split()))
mod=998244353
if d[0]!=0:
      print(0)
      exit()
dd=defaultdict(lambda:0)
for di in d:
      dd[di]+=1
if dd[0]>1:
      print(0)
      exit()
ans=1
for i in set(dd.keys()):
      if i==0:
            continue
      ans*=(dd[i-1]**dd[i])%mod
print(ans%mod)