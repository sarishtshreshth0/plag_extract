H,W = map(int, input().split())

if H > W:
    H,W = W,H

if H == 1:
    print(1)
else:
    N = H * W
    print((N+1)//2)
