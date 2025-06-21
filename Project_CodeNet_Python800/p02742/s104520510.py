import math

H, W = map(int, input().split(' '))

if H == 1 or W == 1:
  print(1)
  exit()

res = math.ceil((H*W)/2)
print(res)

