H,W=map(int,input().split())
if (H==1)|(W==1):
    print(1)
elif (H%2==1)&(W%2==1):
    print(int((H*W+1)/2))
else:
    print(int(H*W/2))