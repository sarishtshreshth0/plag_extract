import sys
n=int(input())
d=list(map(int,input().split()))
if d[0]!=0:
    print(0)
    sys.exit(0)
if n==1:
    print(1)
    sys.exit(0)
for i in range(1,n):
    if d[i]==0:
        print(0)
        sys.exit(0)
dist=[0]*(n) 
for i in range(1,n):
    dist[d[i]]+=1
if dist[1]==0:
    print(0)
    sys.exit(0)
ans=1
mod=998244353
bef=dist[1]
total=dist[1]+1
for i in range(2,n):
    for j in range(dist[i]):
        ans=ans*bef
        ans=ans%mod
    total+=dist[i]
    bef=dist[i]
    if total==n:
        break
    if ans==0:
        break
print(ans)
#print(dist)