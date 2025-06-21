import math
H, W = map(int, input().split())
print(1) if (H == 1) | (W == 1) else print(math.ceil(H*W/2))