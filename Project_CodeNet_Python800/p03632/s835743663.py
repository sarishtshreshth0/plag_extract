a,b,c,d = map(int, input().split())
if a <= b <= c <= d or c <= d <= a <= b:
  print(0)
else:
  ar = sorted([a,b,c,d])
  print(ar[2] - ar[1])