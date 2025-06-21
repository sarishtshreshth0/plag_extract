def resolve():
    H, W = map(int, input().split())
    if H == 1 or W == 1:
        print("1")
    elif H%2 == 1 and W%2 == 1:
        print((H-1)*(W-1)//2+(H-1)//2+(W-1)//2+1)
    elif H%2 == 1 and W%2 == 0:
        print((H-1)*W//2+W//2)
    elif H%2 == 0 and W%2 == 1:
        print(H*(W-1)//2+H//2)
    else:
        print(H*W//2)
resolve()