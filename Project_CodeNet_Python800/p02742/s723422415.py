H,W = map(int,input().split())

if H == 1 or W == 1:
    Ans=1
else:
    if H*W%2 == 0:#マス目の合計が偶数なら
        Ans=H*W/2
    else:#マス目の合計が奇数なら
        Ans=H*W//2+1

print(round(Ans))