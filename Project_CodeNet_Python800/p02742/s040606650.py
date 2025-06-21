H, W = map(int, input().split())
ans = H * W
if H * W in [H, W]:
    print(1)
    exit()
if ans % 2 == 1:
    ans += 1
print(ans // 2)    