h, w = map(int, input().split())

if h == 1 or w ==1:
    print(1)
    exit(0)

if (h * w) % 2 == 0:
    print(int(h * w / 2))
else :
    print(int((h * w + 1) / 2))