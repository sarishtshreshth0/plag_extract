H, W = map(int, input().split())

h = H // 2
w = W // 2

if H == 1 or W == 1:
    print(1)
    exit()

if W % 2 == 1:
    w += 1
if H % 2 == 1:
    print(h * W + w)
else:
    print(h * W)