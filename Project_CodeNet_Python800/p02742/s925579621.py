h,w=map(int, input().split(" "))
if 1 in [h,w]:
  print(1)
elif h * w % 2 == 0:
  print(h * w // 2)
else:
  print(h * w // 2 + 1)