a, b, c = map(int, input().split())
if a > b:
  a, b = b, a
if a <= c <= b:
  print('Yes')
else:
  print('No')