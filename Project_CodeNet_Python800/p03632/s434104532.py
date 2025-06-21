a, b, c, d = map(int, input().split())

seconds = 0

if (b <= c) or (d <= a):
    seconds = 0
elif a - c >= 0:
    if d - b >= 0:
        seconds = b - a
    else:
        seconds = d - a
elif a - c <= 0:
    if b - d >= 0:
        seconds = d - c
    else:
        seconds = b - c
else:
    seconds = "a:{0}, b:{1}, c:{2}, d:{3}".format(a, b, c, d)

print(seconds)