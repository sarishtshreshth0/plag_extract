n=int(input())
s=input()
res=s[0]
ans=1
for i in range(1,n):
  if s[i]==res:
    continue
  else:
    res=s[i]
    ans+=1
print(ans)