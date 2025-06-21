def resolve():
    h, w = map(int, input().split())
    import math
    if w == 1 or h == 1:
        print(1)
    else:
        print(math.ceil(h * w / 2))


if __name__ == '__main__':
    resolve()