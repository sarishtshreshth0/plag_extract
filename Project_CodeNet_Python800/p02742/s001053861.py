h, w = map(int, input().split())
from math import ceil

odd = ceil(h/2) * ceil(w/2)
even = int(h/2) * int(w/2)
if h==1 or w==1:
    print(1)
else:
    print(odd + even)