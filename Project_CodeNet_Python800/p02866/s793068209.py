n=int(input())
d=list(map(int,input().split()))
ans=1 if d[0]<1 else 0
d.sort()
cnt=[0]*(d[-1]+1)
for i in range(n):
  cnt[d[i]]+=1
if cnt[0]!=1:ans=0
mod=998244353
for i in d[1:]:
  ans*=cnt[i-1]
  ans%=mod
print(ans)