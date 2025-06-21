H,W = map(int,input().split())

if H==1 or W==1:
    print(1)
elif H%2==0 and W%2==0 or H%2==0 and W%2==1 or H%2==1 and W%2==0:
    print((H*W)//2)
else:
    print(((H*W)+1)//2)