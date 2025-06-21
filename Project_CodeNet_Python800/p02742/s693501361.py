import math
h,w=map(int,input().split())
if h>1 and w>1:
  print(math.ceil(w/2)*math.ceil(h/2) + (w//2)*(h//2))
else:
  print(1)

