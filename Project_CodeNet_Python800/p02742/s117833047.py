H,W = map(int, input().split())
if H == 1 or W == 1:
    print(1)
else:
    t = H * W
    print(t // 2) if t % 2 == 0 else print((t // 2) + 1)