H, W = map(int,input().split())
if H == 1 or W == 1:
  ans = 1
else:
  ans = int(H*(W/2)) + (H*W % 2)
print(ans)