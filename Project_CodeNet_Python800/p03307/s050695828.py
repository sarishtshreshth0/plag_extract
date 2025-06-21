n = int(input())
def getmdc(x, y):
    while(y):
        x, y = y, x % y
    return x
def mmc2(x):
    return x * 2 // getmdc(x, 2)
print(mmc2(n))