h,w = map(int,input().split())
s = h*w
if h == 1 or w == 1:
    print(1)
elif s%2 == 1:
    print((s//2)+1)
else:
    print(s//2)