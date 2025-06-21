n=int(input())
a=[]
x=str(input())
a.append(x)
d=bool(True)

for i in range(1, n):
  y=str(input())
  if x[len(x)-1]!=y[0]:
    d=False
    
  for j in range(len(a)):
    if y==a[j]:
      d=False
  a.append(y)
  x=y

if  d==True:
  print("Yes")
else:
  print("No")