import math
h,w = map(int,input().split())
if w < h:
  h,w = w,h
if h==1:
  print(1)
else:
  ans = math.ceil((h*w)/2)
  print(max(1,ans))