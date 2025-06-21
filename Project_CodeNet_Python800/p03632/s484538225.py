a, b, c, d = map(int, input().split())

sec = 0
if (a < d and c < b):
    if (a >= c):
        if (b >= d):
            sec = d - a
        else:
            sec = b - a
    else:
        if (b >= d):
            sec = d - c
        else:
            sec = b - c

print(sec)
