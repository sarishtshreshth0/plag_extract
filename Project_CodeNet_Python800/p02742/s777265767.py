H, W = map(int, input().split())
re = H // 2
ro = (H + 1) // 2
ce = W // 2
co = (W + 1) // 2
print(1 if H == 1 or W == 1 else re * ce + ro * co)