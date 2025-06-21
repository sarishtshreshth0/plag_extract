H,W = map(int,input().split())
if H == 1 or W == 1:
  print(1)
a = H * W
b = a // 2
if b != a / 2:
  b += 1
if H != 1 and W != 1:  
  print(b)
