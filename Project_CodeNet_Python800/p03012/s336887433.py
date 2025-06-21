N=int(input())
W=list(map(int,input().split()))
w=sum(W)
ans=10**9
temp=0
for i in W:
  temp+=i
  ans=min(ans,abs(2*temp-w))
print(ans)
