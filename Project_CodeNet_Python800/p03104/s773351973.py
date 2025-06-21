A,B = (int(x) for x in input().split())
if A == 0:
    m = B % 4
    if m == 0:
        print(B)
    elif m == 1:
        print('1')
    elif m == 2:
        print(B^1)
    else:
        print('0')
else:
    ma = (A-1) % 4
    mb = B % 4
    if ma == 0:
        xora = A-1
    elif ma == 1:
        xora = 1
    elif ma == 2:
        xora = (A-1) ^ 1
    else:
        xora = 0
    if mb == 0:
        xorb = B
    elif mb == 1:
        xorb = 1
    elif mb == 2:
        xorb = B ^ 1
    else:
        xorb = 0
    print(xora^xorb)