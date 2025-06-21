import sys
A, B = map(int, input().split())
for i in range(1, 4):
    x = A *B *i
    if ((x % 2) == 1):
      print('Yes')
      sys.exit()
else:
  print('No')