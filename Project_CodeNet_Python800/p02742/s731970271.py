h,w = map(int,input().split())

if w == 1:
  print(1)
  exit()
if h == 1:
  print(1)
  exit()
if w%2 == 0:
  ans = w//2 * h
elif w%2 == 1:
  if h%2 == 0:
    ans = h*w//2
  elif h%2 == 1:
    ans = h*w//2 + 1

print(ans)