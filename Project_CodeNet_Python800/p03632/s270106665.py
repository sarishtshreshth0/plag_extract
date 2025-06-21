a, b, c, d = list(map(int, input().split()))
if d <= a:
    print(0)
    exit()
if a <= c <= b:
    if b >= d:
        print(d - c)
        exit()
    else:
        print(b - c)
        exit()
elif c < a:
    if b >= d:
        print(d - a)
        exit()
    else:
        print(b - a)
        exit()
else:
    print(0)
