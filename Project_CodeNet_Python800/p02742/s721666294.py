import math
data = input().split(' ')
h = int(data[0])
w = int(data[1])
if h == 1 or w == 1:
    print(1)
else:
    ans = math.ceil(h/2) * math.ceil(w/2) + math.floor(h/2) * math.floor(w/2)
    print(ans)