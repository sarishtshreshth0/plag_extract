H, W = [int(_) for _ in input().split()]

if H == 1 or W == 1:
    ans = 1
else:
    ans = (H // 2) * (W // 2) * 2
    if H % 2 == 1:
        ans += W // 2
    if W % 2 == 1:
        ans += H // 2
    if H % 2 == 1 and W % 2 == 1:
        ans += 1
print(ans)
