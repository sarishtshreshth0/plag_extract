M, D = map(int, input().split())
ans=0
for m in range(1,M+1,1):
  for d in range(22,D+1,1):
    d1=d%10
    d10=d//10
    if d1>1 and d10>1:
      if m==d1*d10:
        ans+=1
        
print(ans)