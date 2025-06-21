h, w = list(map(int, input().split()))

masu = h * w

if h == 1:
    print(1)
elif w == 1:
    print(1)
elif h * w % 2 == 0:
    print(int(masu / 2))
else:
    print(int(masu / 2) + 1)
