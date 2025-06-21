H, W = list(map(int, input().split()))
if H==1 or W==1:
    print(1)
    exit()
res = int((H+1)/2) * W
if H%2==1:
    res -= int(W/2)
print(res)
