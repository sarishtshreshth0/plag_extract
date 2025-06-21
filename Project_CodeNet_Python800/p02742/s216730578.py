h,w = map(int,input().split())

if h == 1 or w == 1:
    print(1)
elif (w*h) % 2 == 0:
    print((w*h)//2)
elif (w*h) % 2 == 1:
    print(((w*h)//2)+1)
