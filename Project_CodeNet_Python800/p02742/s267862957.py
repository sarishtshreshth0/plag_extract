H , W = map(int,input().split())

if H == 1 or W ==1:
    print(1)
    exit()

if H %2 == 0:
    tate = H/2
    ans = tate * W

else:
    tate1 = H // 2 + 1
    tate2 = H // 2
    if W % 2 == 0:
        ans = (tate1 + tate2) * W/2
    else:
        ans = tate1*((W//2)+1) + tate2*(W//2)
print(int(ans))
