n=int(input())
f=0
m=n
while m>0:
  f+=m%10
  m//=10
print(['No','Yes'][n%f==0])