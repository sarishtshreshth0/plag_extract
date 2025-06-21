n=int(input())
temp=list(str(n))
a=0
for i in range(0,len(temp)):
  a=a+int(temp[i])
if n%a==0:
  print("Yes")
else:
  print("No")