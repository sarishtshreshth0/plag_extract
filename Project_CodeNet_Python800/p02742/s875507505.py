H, W = map(int, input().split())
count = H * W // 2
if H % 2 == 1 and W % 2 == 1 :
    count +=1
if H == 1 or W == 1:
    count = 1
print(count)