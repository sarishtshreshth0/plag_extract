x, y = map(int, input().split())
if x == 1 or y == 1:
    print(1)
elif (x * y) % 2 == 0:
    print((x * y) // 2)
else:
    print((x * y + 1) // 2)