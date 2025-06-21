
s=list(str(input()))
ans=len(s)
cntx=0
cnty=0
for j in range(len(s)):
  if (int(s[j])==j%2):
    cntx+=1
  if (int(s[j])!=j%2):
    cnty+=1
  ans=min(cntx,cnty)
print(ans)