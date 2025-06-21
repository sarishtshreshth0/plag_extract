H, W = map(int, input().split())

res = 0
if H == 1 or W == 1:
  res = 1
else:
  if (H * W) % 2:
    res = (H * W) // 2 + 1
  else:
    res = (H * W) //2

print(res)