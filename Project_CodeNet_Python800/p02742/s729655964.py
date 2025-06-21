h, w = map(int, input().split())
t = h*w

if h == 1 or w == 1:
  print(1)
else:
  if h % 2 == 1 and w % 2 == 1:
    t = t + 1
  print(int(t/2)) 