import math
tate,yoko = map(int,input().split())
if tate == 1 or yoko == 1:
    print(1)
else:
    if yoko%2 == 0:
        print(int((tate*yoko/2)))
    else:
        print(int((tate*(yoko-1)/2 + math.ceil(tate/2))))
