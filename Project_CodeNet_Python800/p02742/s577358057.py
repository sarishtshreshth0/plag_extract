import math

H,W = list(map(int,input().split(" ")))
if W > 1 and H > 1:
    print(math.ceil((H*W)/2))
else:
    print(1)