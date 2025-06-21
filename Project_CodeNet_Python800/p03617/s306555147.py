import math
q,h,s,d = map(int,input().split())
n = int(input())
value = [0]*4
value[0] = q*4
value[1] = h*2
value[2] = s
value[3] = d/2
dum = min(value)
ind = value.index(dum)
if ind == 0:
    print(value[0]*n)
elif ind == 1:
    print(value[1]*n)
elif ind == 2:
    print(value[2]*n)
else:
    if n == 1:
        value.sort()
        print(value[1])
    elif n%2 == 0:
        print(math.floor(d*n//2))
    else:
        dum1 = (n//2)*d
        value.sort()
        print(math.floor(value[1]+dum1))