H, W = [int(x) for x in input().split(" ")]
if H > W:
    H, W = W, H
if H == 1:
    print(1)

elif H % 2 == 0:
    print(W * (H // 2))
else:
    if W % 2 == 0:
        print(W * H // 2)
    else:
        print(((W - 1) * H // 2) + H // 2 + 1)
