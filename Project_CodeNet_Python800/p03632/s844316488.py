a, b, c, d = list(map(int, input().split()))

if a > c:
    minx = a
elif a <= c:
    minx = c

if b <= d:
    maxy = b
elif b > d:
    maxy = d

if minx >= maxy:
    print(0)
elif minx < maxy:
    print(maxy - minx)