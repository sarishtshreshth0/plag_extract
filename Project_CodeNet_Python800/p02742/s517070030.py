H,W=map(int,input().strip().split())

if H == 1 or W == 1:
    print(1)
elif H % 2 == 0:
    print((H//2)*W)
else:
    sets = W // 2
    sum = ((H//2)*2+1)*sets
    if W % 2 == 1:
        sum += ((H//2) + 1)
    print(sum)