N=int(input())
import collections
l=list(map(int,input().split()))
cnt=collections.Counter(l)
if cnt[0] > 1 or l[0] != 0:
   print(0)
   exit()
ans=1
mod=998244353
for i in range(1,max(cnt)):
   ans*=pow(cnt[i],cnt[i+1],mod)
   ans%=mod
print(ans)