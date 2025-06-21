h,w = map(int,input().split())
resp = h*w//2
if h == 1 or w == 1:
    print(1)
else:
    if (h * w) % 2 != 0:
        resp += 1
        print(resp)

    elif (h*w) % 2 == 0:
        print(resp)
