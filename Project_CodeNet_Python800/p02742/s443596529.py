H, W = map(int, input().split())

if H >= 2 and W >= 2:
    if H % 2 == 0:
        print((H * W) // 2)
    else:
        print(((H - 1) * W) // 2 + (W + 1) // 2)
else:
    print(1)
