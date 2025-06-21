def resolve():
    import math
    a, b = map(int, input().split())
    if a == 1:
        bina = 0
    elif a == 2:
        bina = 1
    elif a == 3:
        bina = 3
    elif a%4 ==3:
        bina = a
    else:
        lowera = math.floor((a - 3) / 4) * 4 + 3
        bina = 0
        for i in range(lowera + 1, a):
            bina = bina ^ i

    if b ==1:
        binb = 1
    elif b ==2:
        binb = 3
    elif b==3:
        binb =0
    else:
        if b%4 == 3:
            binb = 0
        else:
            lowerb = math.floor((b-3)/4)*4+3
            binb = 0
            for j in range(lowerb+1, b+1):
                binb = binb^j

    print(bina^binb)
resolve()