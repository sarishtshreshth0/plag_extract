H,W = map(int,input().split())
P = H*W

if H == 1 or W ==1:
  print(1)

elif P%2 == 0:
  print(int(P/2))
else:
  print(int(P/2)+1)