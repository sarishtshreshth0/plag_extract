import math
H,W = map(int,input().split())
if H > 1 and W > 1:
    ans = math.ceil(H*W/2)
else:
    ans = 1
print(ans)
