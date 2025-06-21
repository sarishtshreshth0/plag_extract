a, b = list(map(int, input().split()))
if a == 1:
  a = 14
else:
  a = a
if b == 1:
  b = 14
else:
  b = b
if a > b:
  print('Alice')
elif a == b:
  print('Draw')
else:
  print('Bob')
