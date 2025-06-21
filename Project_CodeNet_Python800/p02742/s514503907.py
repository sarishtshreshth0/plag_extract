H,W = map(int,input().split())
if H == 1 or W == 1:
  print(1)
  exit(0)
else:
  result = H * W
  if result % 2 == 0:
    print(result // 2)
  else:
    print(result // 2 + 1)