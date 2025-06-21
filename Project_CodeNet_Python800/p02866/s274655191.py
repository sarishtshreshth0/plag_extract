N=int(input())
D=list(map(int,input().split()))

isOK=True
if D[0]!=0:
    isOK=False

for i in range(1,N):
    if D[i]==0:
        isOK=False
        break

cnt=[0]*(max(D)+1)
MOD=998244353
for i in range(N):
    cnt[D[i]]+=1

ans=1
for i in range(len(cnt)-1):
    
    for r in range(cnt[i+1]):
        ans=ans*cnt[i]%MOD
if isOK:
    print(ans)
else:
    print(0)