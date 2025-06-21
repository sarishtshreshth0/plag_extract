a,b=map(int,input().split())
s=input()
if s[a]!="-":
  print("No")
else:
  cnt=0
  for i in range(a+b+1):
    if s[i]=="-":
      cnt+=1
  if cnt!=1:
    print("No")
  else:
    print("Yes")