H,W = map(int,input().split())
if H ==1 or W ==1:
  print(1)
else:
  a = H*W
  if a%2 == 0:
    print(int(a/2))
  else:
    print(int(a/2)+1)