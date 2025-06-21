m, d = map(int, input().split())
if m < 4 or d < 22:
  print("0")
else:
  res=0
  for i in range(22, d+1):
    d1, d2 = int(i/10), i%10
    if d2 < 2:
      continue
    res += 1 if d1*d2<=m else 0
  print(res)