w,h = map(int, input().split())
x = w*h

if h !=1 and w != 1:
    print((h*w+1)//2)
else:
    print(1)