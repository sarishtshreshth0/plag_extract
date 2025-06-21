a, b = map(int, input().split())
sn = input()

result = True
for i in range(len(sn)):
  if (i == a+1-1) and (sn[i] != "-"):
    result = False
    break
  else :  
    if (i != a+1-1) and ( ord(sn[i]) < 48) or ( 57 < ord(sn[i])):
      result = False
      break

if result:
  print("Yes")
else :
  print("No")