def resolve():
    H, W = [int(i) for i in input().split()]
    if min(H, W) == 1:
        print(1)
    elif (H * W) % 2 == 0:
        print(format(H * W // 2, "d"))
    else:
        print(format((H * W // 2) + 1, "d"))


resolve()
