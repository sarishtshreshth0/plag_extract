import sys
H, W = [int(x) for x in input().split()]
if(H==1)or(W==1):
  print(1)
  sys.exit()
if(H%2)==0:
  h = -(-H//2)
  print(h*W)
  sys.exit()
elif(W%2)==0:
  w = -(-W//2)
  print(H*w)
  sys.exit()
else:
  print(-(-(H*W)//2))
  sys.exit()