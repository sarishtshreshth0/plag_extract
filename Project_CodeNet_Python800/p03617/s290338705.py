y=list(map(int, input().split()))
N=int(input())
ans=0

if N>=2:
  tmp=min(y[0]*8, y[1]*4, y[2]*2, y[3])
  rep=N//2
  ans+=rep*tmp
  N-=rep*2

if N==1:
  ans+=min(y[0]*4, y[1]*2, y[2])

print(ans)