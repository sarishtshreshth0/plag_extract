A, B, C = map(int, input().split())
if 0 < (C - A) / (B - A) <= 1:
  print('Yes')
else:
  print('No')
