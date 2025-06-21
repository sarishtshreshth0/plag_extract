n=int(input())
s=input()

bef=s[0]
ans=1
for i in s[1:]:
  if i !=bef:
    ans+=1
    bef=i
print(ans)