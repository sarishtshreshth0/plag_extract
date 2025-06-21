import math
H, W = list(map(int, input().split()))

sum = float(H*W)
if sum%2 == 0:
    if H == 1 or W == 1:
        print(1)
    else:
        print(H*W//2)
else:
    if H == 1 or W == 1:
        print(1)
    else:
        print(math.floor(H*W/2)+1)