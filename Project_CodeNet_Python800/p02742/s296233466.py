x = list(map(int,input().split()))
H = x[0]
W = x[1]

if H == 1 or W == 1:
    print(1)
else:
    if W % 2 == 0:
        print(int(H*W/2))
    else:
        if H % 2 == 0:
            print(int(H*(W-1)/2 + H/2))
        else:
            print(int(H*(W-1)/2 + (H+1)/2))
