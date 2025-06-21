x=int(input())
li=list(str(x))
s=0
for i in li:
  s+=int(i)
if x%s==0:
  print("Yes")
else:
  print("No")