list = list(map(int,input().split()))
if list[0] <= list[2] <= list[1] or list[0] >= list[2] >= list[1]:
  print("Yes")
else:
  print("No")