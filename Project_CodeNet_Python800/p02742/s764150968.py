H,W = [int(i) for i in input().split()]
if H == 1 or W == 1:
    print(1)
else:
    print(int((H*W)/2 + 0.5))