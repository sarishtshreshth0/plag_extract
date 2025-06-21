#!/usr/bin/env python
import math

h, w = map(int, input().split())
if h==1 or w==1:
    ans = 1 
else:
    ans = math.ceil(h*w/2)
print(ans)
