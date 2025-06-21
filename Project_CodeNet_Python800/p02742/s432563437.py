H, W = list(map(int, input().split()))

seki = H * W

if H == 1 or W == 1:
    print(1)
else:
    ans = (seki + 2 - 1) // 2
    print(ans)
