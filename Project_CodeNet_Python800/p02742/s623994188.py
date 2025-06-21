import numpy as np

l = list(map(int, input().split()))
a = l[0]
b = l[1]

if not(a==1 or b==1):
    if a*b %2==0:
        print(int(a*b/2))
    else:
        print(int(a*b/2+1))

else:
    print(1)
