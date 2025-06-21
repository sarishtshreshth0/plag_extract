M,D=map(int,input().split())
ans=0
for i in range(D+1):
  if(i>=10):
    X=i//10
    Y=i%10
    if(X>=2 and Y>=2):
      if(X*Y<=M):
        ans+=1
print(ans)