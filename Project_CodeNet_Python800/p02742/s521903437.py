H, W = map(int,input().split())
if H == 1 or W == 1:
    print(1)
else:
    ans = H*W
    if ans % 2:
        print(ans//2+1)
    else:
        print(ans//2)