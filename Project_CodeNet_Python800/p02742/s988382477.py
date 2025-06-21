import math
h,w = map(int,input().split())
w1 = int(w/2)
h1 = int(h/2)
w2 = int(w/2)
h2 = int(h/2)
if ( w % 2 != 0 ):
  w1 += 1
if ( h % 2 != 0 ):
  h1 += 1
res = h1 * w1 + h2 * w2
if (h == 1 or w == 1):
  print(1)
else:
  print(res)