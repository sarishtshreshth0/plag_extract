H, W = [int(n) for n in input().split()]
if H == 1 or W == 1:
    print(1)
elif H%2 == 0:
    print(H*W//2)
else:
    h = (H+1)//2
    h_ = h-1
    if W%2 == 0:
        print((h+h_)*W//2)
    else:
        print((h+h_)*(W//2) + h)
