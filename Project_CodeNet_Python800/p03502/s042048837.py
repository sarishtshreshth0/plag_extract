N=input()
a=int(N)
b=list(N)
sum=0

for i in b:
  sum+=int(i)
 
if a%sum==0:
  print('Yes')
else:
  print('No')
