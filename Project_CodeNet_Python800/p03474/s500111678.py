a,b=map(int,input().split())
S=input()
flag = True

for i in range(len(S)):
  if i == a:
    if not S[a]=="-":
      flag = False
  else:
    if not S[i].isnumeric():
      flag = False
if flag:
  print("Yes")
else:
  print("No")