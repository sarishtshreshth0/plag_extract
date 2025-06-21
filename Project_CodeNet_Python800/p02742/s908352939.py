def resolve():
    H, W = list(map(int, input().split()))
    ans = 0
    if (H == 1 or W == 1):
        print(1)
        return
    if H % 2 == 1:
        even = (H // 2) + 1
    else:
        even = (H // 2)

    odd = H - even

    if W % 2 == 1:
        ans += even * (W // 2 + 1)
    else:
        ans += even * (W // 2)

    ans += odd * (W // 2)

    print(ans)

    return
 
resolve()