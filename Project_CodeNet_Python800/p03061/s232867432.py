n = int(input())
a = list(map(int,input().split()))

from fractions import gcd
import math

llis = [0]
rlis = [0]
for i in range(n):
    llis.append(gcd(llis[-1],a[i]))
    rlis.append(gcd(rlis[-1],a[n-i-1]))

mx = 0
for i in range(n):
    cd = gcd(llis[i],rlis[n-i-1])
    mx = max(mx,cd)

print(mx)
