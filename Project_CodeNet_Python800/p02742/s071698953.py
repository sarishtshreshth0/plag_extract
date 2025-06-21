H, W = map(int, input().split())
if H == 1 or W == 1:
  r = 1
else:
  r = (H*W +2-1)//2
print(r)
