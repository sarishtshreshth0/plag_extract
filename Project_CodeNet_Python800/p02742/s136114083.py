import sys
readline = sys.stdin.readline

H,W = map(int,readline().split())

if H == 1 or W == 1:
  print(1)
  exit(0)
  
if (H * W) % 2 == 1:
  print((H * W) // 2 + 1)
else:
  print((H * W) // 2)