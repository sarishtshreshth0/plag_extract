def resolve():
    H, W = list(map(int, input().split()))
    if H == 1 or W == 1:
        print(1)
        return

    ans = int(H * W / 2)
    if ((H * W) % 2 == 1):
        ans += 1
    print(ans)
    return
 
resolve()