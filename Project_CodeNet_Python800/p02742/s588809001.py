H, W = map(int, input().split())

ans = 0
if H == 1 or W == 1:
  ans = 1
else:
  if (H % 2 == 0) and (W % 2 == 0):
    ans = (H * W) // 2
  if (H % 2 == 0) and (W % 2 == 1):
    ans = (H // 2) * W
  if (H % 2 == 1) and (W % 2 == 0):
    ans = H * (W // 2)
  if (H % 2 == 1) and (W % 2 == 1):
    ans = (H * W) // 2 + 1

print(ans)
