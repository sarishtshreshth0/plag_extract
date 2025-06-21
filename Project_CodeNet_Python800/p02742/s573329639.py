h, w = map(int, open(0).read().split())

if h == 1 or w == 1:
    print(1)
else:
    print(sum(divmod(h*w, 2)))