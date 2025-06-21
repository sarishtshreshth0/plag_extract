H, W = map(int, input().split())

ans = 0
x = H * W

if H == 1 or W == 1:
    ans = 1
elif x % 2 == 0:
    ans = x // 2
else:
    ans = (x // 2) + 1

print(ans)