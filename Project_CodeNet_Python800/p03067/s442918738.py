a, b, c = [int(i) for i in input().split()]
if a < c < b or a > c > b:
  print("Yes")
else:
  print("No")