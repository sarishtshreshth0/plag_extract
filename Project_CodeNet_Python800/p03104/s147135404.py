a,b = map(int,input().split())

def calc(x):
    l = len(format(x,'b'))
    s = '1' if x%4==1 or x%4==2 else '0'
    for i in range(1,l):
        x_ = x
        x_ -= 2**i-1
        mod = x_ % (2**(i+1))
        if mod >= 2**i:
            s += '0'
        else:
            if mod%2==0:
                s += '0'
            else:
                s += '1'
    s = s[::-1]
    return s

suma = int(calc(a-1),2)
sumb = int(calc(b),2)
print(int(suma^sumb))