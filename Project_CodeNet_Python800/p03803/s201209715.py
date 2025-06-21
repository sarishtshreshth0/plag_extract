n = input().split()
a = int(n[0])
b = int(n[1])
if a == 1:
  a = 14
if b == 1:
  b = 14
if a > b:
  print('Alice')
elif a < b:
  print('Bob')
else:
  print('Draw')
