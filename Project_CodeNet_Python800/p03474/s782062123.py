a,b=map(int, input().split())
s=input()
flag=True
for i in range(a+b+1):
  if s[a]!="-":
    flag=False
  elif i!=a and not s[i].isdigit():
    flag=False
print("Yes" if flag else "No")