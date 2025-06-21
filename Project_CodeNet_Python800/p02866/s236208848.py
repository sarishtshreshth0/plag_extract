N=int(input())
D=list(map(int,input().split()))
mod=998244353
ans=1
count=[0 for i in range(0,N)]
for i in range(0,N):
    count[D[i]]+=1

able=True
if D[0]!=0 or count[0]!=1:
    able=False
for i in range(0,N-1):
    if count[i]==0 and count[i+1]!=0:
        able=False

if able:
    for i in range(0,N-1):
        ans=(ans*pow(count[i],count[i+1],mod))%mod
    print(ans)
else:
    print(0)