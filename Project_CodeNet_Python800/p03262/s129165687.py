import math
import sys
def gcd(l: list):
    n=len(l)
    gcd=math.gcd(l[0],l[1])
    for i in range(2,n):
        gcd=math.gcd(l[i],gcd)

    return gcd

n, x=map(int,input().split())
x_list=list(map(int,input().split()))

if n==1:
    print(abs(x_list[0]-x))
    sys.exit()


y=[0]*n
for i in range(n):
    y[i]=abs(x_list[i]-x)

print(gcd(y))