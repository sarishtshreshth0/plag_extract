h, w = map(int, input().split())

if h != 1 and w != 1:
    if h % 2 == 0:
        print(int(h / 2 * w))
    elif w % 2 == 0:
        print(int(w / 2 * h))
    else:
        print(int((h // 2 + 1) * w - w // 2))
else:
    print(1)
