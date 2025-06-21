def readInt():
    return list(map(int, input().split()))
    
h, w = readInt()
if h == 1 or w == 1:
    print(1)
elif h*w%2 == 0:
    print(h*w//2)
else:
    print(h*w//2+1)
    
