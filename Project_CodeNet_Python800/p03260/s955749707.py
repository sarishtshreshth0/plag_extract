a, b = map(int, input().split())
x = a * b
r = x % 2

if r == 1:
  print('Yes')
else:
  print('No')