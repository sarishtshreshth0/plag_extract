h,w = map(int, input().split())

if h == 1 or w == 1:
    print(1)
else:
    if h % 2 == 0:
        print(int((h / 2) * w))
    else:
        if w % 2 == 0:
            print(int(((h//2) * w/2) + ((h//2 + 1) * w/2)))
        else:
            print(int(((h//2 + 1) * (w//2+1)) + ((h//2) * (w//2))))
