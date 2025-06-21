import math
H,W=map(int,input().split())
if W==1:
    print(1)
elif H==1:
    print(1)
else:
    A=math.ceil(H*W/2)
    print(A)