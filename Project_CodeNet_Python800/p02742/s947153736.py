import math
h,w=map(int,input().split())

if h>1 and w>1:
  if h*w%2==0:
    print(int((h*w)/2))
  else:
    print(int((h*w)/2+1))
  
else:
  print(1)