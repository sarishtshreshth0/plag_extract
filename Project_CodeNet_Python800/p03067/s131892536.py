a, b, c = list(map(int, input().split()))

if (c - a) * (c - b) < 0:
  print("Yes")
else:
  print("No")