import math as m

h,w = map(int, input().split())

if (h==1) or (w==1):
    print(1)
else:
    print(m.ceil(h*w/2))