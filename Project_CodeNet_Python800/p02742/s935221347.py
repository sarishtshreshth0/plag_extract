import numpy as np

h, w = map(int, input().split())

if h == 1 or w == 1:
  print(1)
else:
  print(int(np.ceil(h*w/2)))