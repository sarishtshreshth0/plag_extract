H, W = map(int, input().split())

if H == 1 or W == 1:
    print(1)
else:
    print(H * W // 2 if H * W % 2 == 0 else H * W // 2 + 1)