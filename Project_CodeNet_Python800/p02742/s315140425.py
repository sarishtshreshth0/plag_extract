h, w = map(int, input().split())

print(1) if h == 1 or w == 1 else print((h * w + 1) // 2)