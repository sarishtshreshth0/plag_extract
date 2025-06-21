n=int(input())
a=list(map(int,input().split()))

import math

del_0=a[0]

if n==2:
    print(max(a))
    exit()
#print(a)
for i in range(n):
    #print(">>>>>>>>>",i+1)
    if i==2:
        del_1=max([math.gcd(a[0],a[1]),math.gcd(a[2],a[1]),math.gcd(a[2],a[0])])
        #print(([math.gcd(a[0],a[1]),math.gcd(a[2],a[1]),math.gcd(a[2],a[0])]))
    elif i>2:
        del_1=max(del_0,math.gcd(del_1,a[i]))
        #print(del_1)

    del_0=math.gcd(del_0,a[i])
    #print(del_0)
print(del_1)