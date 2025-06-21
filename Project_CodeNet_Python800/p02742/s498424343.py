h, w = map(int, input().split())
if h==1 or w == 1:
  print(1)
else:
  ans = h * w //2 + (h*w)%2
  print(ans)