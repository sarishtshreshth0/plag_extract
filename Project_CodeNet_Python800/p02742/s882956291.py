H, W = map(int,input().split())
if H>1 and W>1 :
    print(int(H/2)*W  + (int(W/2)+W%2)*(H%2))
else :
    print(1)