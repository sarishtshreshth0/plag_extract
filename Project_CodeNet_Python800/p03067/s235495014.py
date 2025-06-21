a = list(map(int,input().split()))
if a[1] > a[0]:
  if a[1] < a[2] or a[2] < a[0]:
    print("No")
  else:
  	print("Yes")
else:
  if a[1] > a[2] or a[2] > a[0]:
    print("No")
  else:
    print("Yes")