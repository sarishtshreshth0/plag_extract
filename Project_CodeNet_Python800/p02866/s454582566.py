mod=998244353
n=int(input())
from collections import Counter as co
j=list(map(int,input().split()))
l=co(j)
ll=len(l)
for i in range(ll):
    if i not in l:print(0);exit()
if l[0]>=2 or j[0]!=0:print(0);exit()
ans=1
pre=1
for k,v in sorted(l.items()):
    ans*=pow(pre,v,mod)
    ans%=mod
    pre=v
print(ans%mod)