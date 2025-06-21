a, b = map(int, input().split())
def calc(x):
    rtn = 0
    i = 1
    while i<=x:
        i *= 2
        if i==2:
            if x%4==1 or x%4==2:
                rtn += 1
            continue
        if x%i<i//2:
            continue
        rtn += ((x%i-i//2+1)%2)*(i//2)
    return rtn
if a==0:
    print(calc(b))
else:
    print(calc(a-1)^calc(b))