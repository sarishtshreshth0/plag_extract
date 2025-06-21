def resolve():
    from math import ceil
    h, w = map(int, input().split())
    if h <= 1 or w <= 1:
        print(1)
    elif h * w % 2 == 0:
        print(int(h * w / 2))
    else:
        print(int(ceil(h * w / 2)))


resolve()