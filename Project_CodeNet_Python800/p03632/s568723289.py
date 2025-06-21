a, b, c, d = map(int, input().split(" "))

if a <= c:
  if b <= c:
    ans = 0
  elif d <= b:
    ans = d - c
  else:
    ans = b - c
else:
  if d <= a:
    ans = 0
  elif b <= d:
    ans = b - a
  else:
    ans = d - a
print(ans)