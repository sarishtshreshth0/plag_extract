a, b, c, d = map(int, input().split())

if d <= a or b <= c:
  print(0)
elif c <= a and b <= d:
  print(b-a)
elif a <= c and b <= d:
  print(b-c)
elif c <= a and d <= b:
  print(d-a)
elif a <= c and d <= b:
  print(d-c)
else:
  print(0)
