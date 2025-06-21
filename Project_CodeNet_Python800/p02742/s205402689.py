import math
H, W = map(int, input().split())
A = math.ceil((H * W)/2)

if H == 1 or W == 1:
    print(1)
else:
    print(A) 
