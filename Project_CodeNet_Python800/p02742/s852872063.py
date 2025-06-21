H,W = [int(n) for n in input().split()]
if H < 2:
  W = 1
if W < 2:
  H = 1
print((H*W//2) if H*W%2==0 else ((H*W+1)//2))