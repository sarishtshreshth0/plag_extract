import math
h, w = [int(w) for w in input().split()]

if h == 1 or w == 1:
    print(1)
else:
    print(math.ceil(h * w / 2))
