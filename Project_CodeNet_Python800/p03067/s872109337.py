a = list(map(int,input().split()))

if (a[0] < a[2] and a[2] < a[1] ) or (a[0] > a[2] and a[2] > a[1]):
  print("Yes")
else:
  print("No")