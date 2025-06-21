a, b, c, d = map(int, input().split())

if a > c:
  maxac = a
else:
  maxac = c
if b < d:
  minbd = b
else:
  minbd = d

res = minbd - maxac
if res < 0:
  print(0)
else:
  print(res)