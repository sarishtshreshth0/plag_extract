n=int(input())
m=str(n)
x=0
for i in m:
  x+=int(i)
if n%x==0:
  print('Yes')
else:
  print('No')
