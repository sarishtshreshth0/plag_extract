m,d=map(int,input().split())
ans=0
for i in range(2,m+1):
  for j in range(22,d+1):
    s=str(j)
    if int(s[1])<2:
      continue
    if i==int(s[0])*int(s[1]):
      ans+=1
print(ans)