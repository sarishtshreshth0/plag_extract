n,k=map(int, input().split())
ans=1
while 1:
  n//=k
  if n>0: ans+=1
  else: break
print(ans)