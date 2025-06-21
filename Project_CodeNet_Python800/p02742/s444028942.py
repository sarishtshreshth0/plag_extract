H, W = map(int, input().split())
if H == 1 or W == 1:
    ans = 1
else:
    if H % 2:
        if W % 2:
            ans = ((H // 2 + 1) * (W // 2 + 1)) + ((H // 2) * (W // 2))
        else:
            ans = ((H // 2 + 1) + (H // 2)) * (W // 2)
    else:
        ans = H / 2 * W
print(int(ans))
