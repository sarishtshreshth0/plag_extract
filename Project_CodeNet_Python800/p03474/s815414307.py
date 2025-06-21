a,b=map(int,input().split())
s=input()

ans="No"

if s[a]=="-":
  if s[:a].isdigit() and s[a+1:].isdigit():
    ans="Yes"

print(ans)