import math

H, W = map(int, input().split())
    
ans = int(H / 2) * W
if (H % 2) == 1:
    ans += math.ceil(W / 2)

if H == 1 or W == 1:
    ans = 1

print(ans)