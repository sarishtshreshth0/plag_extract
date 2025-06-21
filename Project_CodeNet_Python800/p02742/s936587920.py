x,y = map(int,input().split())



if x ==1 or y ==1:
  print(1)
  exit(0)
if x%2==0 or y%2==0:
  print(int(x/2*y))
  exit(0)
a=int(x*y/2)+1
print(a)
