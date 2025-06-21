h,w = map(int,input().split())


if w == 1 or h == 1:
    print(1)
elif w%2 != 0 and h%2 != 0:
    print((w*h+1)//2) 
else:
    print(w*h//2)