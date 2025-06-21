import math
 
H, W = map(int, input().split())
 
print(1 if (H == 1 or W == 1) else math.ceil(W*H/2))