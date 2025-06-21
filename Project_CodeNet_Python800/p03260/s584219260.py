A,B = map(int, input().split())
if 1*A*B %2 != 0 or 2*A*B %2 != 0 or 3*A*B %2 != 0:
  print('Yes')
else:
  print('No')