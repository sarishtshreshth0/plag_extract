H, W = map(int, input().split())

if H > 1 and W > 1:
  if H*W % 2 == 0:
    s = (H * W) // 2
  elif H*W % 2 != 0:
    s = (H * W + 1) // 2

elif H == 1 or W  == 1:
  s = 1


print(s)