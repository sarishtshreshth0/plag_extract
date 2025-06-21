# B - Bishop

H, W = map(int, input().split())

ans = W * (H//2)
if H&1:
    ans += (W+1)//2

if H == 1 or W == 1:
    ans = 1

print(ans)