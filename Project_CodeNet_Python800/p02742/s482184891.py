# B - Bishop
H,W = map(int,input().split())
if H>1 and W>1:
    print((H*W+1)//2)
else:
    print(1)