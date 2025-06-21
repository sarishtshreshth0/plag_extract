H, W = map(int, input().split())
if (H==1 or W==1):
    print(1)
elif (H%2==0):
    H /=2
    print(int(H*W))
else:
    H //= 2
    if(W%2==0):
        print(int(H*W+(W/2)))
    else:
        print(int(H*W+(W//2+1))) 
