H, W = map(int, input().split())

if min(H,W) == 1:
    print(1)
elif H*W % 2 == 0:
    print(int(H*W/2))
else:
    print(int(H*W/2)+1)


