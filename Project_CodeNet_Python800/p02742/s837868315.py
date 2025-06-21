h,w = [int(x) for x in input().split()]

if h == 1 or w == 1:
    print(1)
else:
    print(((h*w)+1) // 2)