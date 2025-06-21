a, b = map(int, input().split())

if a==1 or b==1:
  if a>b:
    print('Bob')
  elif b>a:
    print('Alice')
  else:
    print('Draw')
else:
  if a>b:
    print('Alice')
  elif b>a:
    print('Bob')
  else:
    print('Draw')