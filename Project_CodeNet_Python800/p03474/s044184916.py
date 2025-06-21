a,b=map(int,input().split())
s=input()
if s[a]!="-":
  print("No")
  exit()
for i in (s[:a]+s[a+1:]):
  if i not in "0123456789":
    print("No")
    exit()
print("Yes")