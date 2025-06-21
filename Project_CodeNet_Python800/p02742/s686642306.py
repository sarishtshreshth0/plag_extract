h,w = map(int,input().split())
c = 0
if w%2 == 0:
    c = (w//2)*h
else:
    if h%2 == 0:
        c = (h//2)*w
    else:
        c = ((h//2)+1)*((w//2)+1)+(h//2)*(w//2)

if h == 1 or w == 1:
    c = 1
print(c)