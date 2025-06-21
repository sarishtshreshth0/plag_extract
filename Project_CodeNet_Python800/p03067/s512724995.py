a = list(map(int, input().split()))
b = sorted(a)
if a[2] == b[1]:
  print("Yes")
else:
  print("No")