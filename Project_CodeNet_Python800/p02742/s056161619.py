h,w = [int(i) for i in input().split()]
if h == 1 or w == 1:
    print(1)
elif h % 2 == 1 and w % 2 == 1:
    print(int(h*w/2) + 1)
else:
    print(int(h*w/2))