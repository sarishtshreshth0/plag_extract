H,W = list(map(int,input().split()))
if H == 1 or W == 1:
  print(1)
  exit()
HE = H//2
HO = H - HE
WE = W//2
WO = W - WE
print(HO*WO+HE*WE)