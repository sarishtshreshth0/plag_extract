H,W = map(int, input().split())
if H == 1 or W == 1:
    print(1)
else:
    div,mod = divmod(H*W,2)
    print(div+mod)