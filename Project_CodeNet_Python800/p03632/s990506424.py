a, b, c, d = map(int, input().split())
if a < c:
    if c < b and b < d:
        print(b - c)
    elif c < b and d <= b:
        print(d - c)
    else:
        print(0)
else:
    if a < d and d < b:
        print(d - a)
    elif a < d and b <= d:
        print(b - a)
    else:
        print(0)
