n,k=map(int,input().split())
i=0
ans=0
while k**i <= n:
  ans+=1
  i+=1
print(ans)