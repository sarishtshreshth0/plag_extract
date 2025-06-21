H, W = map(int, input().split())
h_odd = 1 if H%2 == 1 else 0
if H == 1 or W == 1:
    print("1")
else:
    if h_odd == 1:
        H += 1
    print(W * H//2 - int(W//2 + 2**-1) * h_odd)
