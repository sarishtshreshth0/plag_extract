h, w = map(int, input().split())

ans = h*w
if h == 1 or w == 1:
  print(1)
else:
  if ans%2 == 0:
    print(ans//2)
  else:
    print(ans//2+1)
