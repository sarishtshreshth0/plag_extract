a,b = map(lambda x:int(x),input().split())
if a==1 or b==1:
  print(1)
else:
  print(int((a*b)/2+(a*b)%2))