import math
h, w = map(int,input().split())
if w == 1 or h == 1:
    print(1)
else:
    count = 0
    if h % 2 != 0:
        count += math.ceil(w / 2)
    count += w * math.floor(h / 2)
    print(count)