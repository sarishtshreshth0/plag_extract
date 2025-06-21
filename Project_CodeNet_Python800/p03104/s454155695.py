a, b = map(int, input().split())
if a == b:
    print(a)
else:
    if a % 2 == 0 and b % 2 == 1:
        if (b-a+1) % 4 == 0:
            print(0)
        else:
            print(1)
    elif a % 2 == 0 and b % 2 == 0:
        if (b-a) % 4 == 0:
            print(b)
        else:
            print(b^1)
    elif a % 2 == 1 and b % 2 == 1:
        if (b-a) % 4 == 0:
            print(a)
        else:
            print(a^1)
    elif a % 2 == 1 and b % 2 == 0:
        if (b-a-1) % 4 == 0:
            print(a^b)
        else:
            print((a^b)^1)