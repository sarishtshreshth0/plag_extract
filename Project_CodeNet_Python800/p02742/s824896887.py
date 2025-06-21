H, W = map(int, input().split())

if H == 1 or W == 1:
  print(1)
  exit()

tmp = H * W

if tmp % 2 == 0:
  print(tmp // 2)
else:
  print(tmp // 2 + 1)
