h, w = map(int, input().split())
if h == 1 or w == 1:
    p = 1
elif h*w%2 == 0:
    p = h*w/2
elif h*w%2 != 0:
    p = h*w/2+1
print(int(p))