H,W = (int(x) for x in input().split())
if H==1 or W==1:
  print(1)
elif (H*W)%2:
  print((H*W-1)//2 + 1)
else:
  print((H*W)//2)