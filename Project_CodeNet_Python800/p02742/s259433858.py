H, W = map(int, input().split())

if W == 1:
    print(1)
elif H == 1:
    print(1)
else:
    ans = W * (H // 2)
    if H % 2 == 1:
        if W % 2 == 0:
            ans += W // 2
        else:
            ans += W // 2 + 1
    print(ans)
