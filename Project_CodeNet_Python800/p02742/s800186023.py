h,w = list(map(int, input().split()))

if h==1 or w==1:
    print(1)
else:
    q,r = divmod(h*w, 2)
    print(q+r)