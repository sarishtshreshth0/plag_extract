h, w = list(map(int, input().split()))

s = 0

if h == 1 or w == 1:
    s = 1
else:
    s = h*w//2 + h*w % 2

print(s)


