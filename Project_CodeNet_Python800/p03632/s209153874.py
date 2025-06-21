a, b, c, d = map(int, input().split())
if a < c:
  if b < c:
    print(0)
  elif d > b:
    print(b-c)
  else:
    print(d-c)
else:
  if a > d:
    print(0)
  elif b > d:
    print(d-a)
  else:
    print(b-a)