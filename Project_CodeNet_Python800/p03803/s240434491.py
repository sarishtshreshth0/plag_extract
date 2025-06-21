a,b = map(int,input().split())
if a==b:
  print('Draw')
elif a==1 and b == 13:
  print('Alice')
elif a==13 and b==1:
  print('Bob')
elif a > b:
  print('Alice')
elif b > a:
  print('Bob')