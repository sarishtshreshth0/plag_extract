import math
h,w=map(int,input().split())
if h>2 and w>1:
    print(math.ceil(h*w/2))
if h==1 or w==1:
    print(1)