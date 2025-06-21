def f(x):
    cou = 0
    re = 0
    while True:
        if x < 2**cou:
            break
        if cou == 0:
            if 1 <= x % 4 <= 2:
                re += 1
        else:
            p = x % (2**(cou+1))
            if 2**cou <= p and p % 2 == 0:
                re += 2**cou
        cou += 1
    return re
a , b = map(int,input().split())

print(f(a-1) ^ f(b))