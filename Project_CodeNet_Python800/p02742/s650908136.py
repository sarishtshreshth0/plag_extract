a,b=map(int, input().split())
if a==1 or b==1:
  print(1)
elif a*b%2==0:
  print(a*b//2)
else:
  print(a*b//2+1)