H, W = map(int, input().split())

if (H*W) % 2 == 0:
  if H == 1 or W == 1:
    res = 1
  else:
    res = int(H * W / 2)
else:
  if H == 1 or W == 1:
    res = 1
  else:
    res =  int(H * (W//2) + int(H/2) + 1)
print('{0:d}'.format(res))