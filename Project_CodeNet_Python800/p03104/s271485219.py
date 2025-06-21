a, b = map(int, input().split())
rec = 0
len = b - a + 1
if a % 2 == 0:
    if len % 2 == 1:
        if (len - 1) % 4 == 0:
            rec = b
        else:
            rec = 1^b
    else:
        if len % 4 == 0:
            rec = 0
        else:
            rec = 1
else:
    if len % 2 == 0:
        if (len - 2) % 4 == 0:
            rec = a^b
        else:
            rec = a^1^b
    else:
        if (len - 1) % 4 == 0:
            rec = a
        else:
            rec = a^1
print(rec)