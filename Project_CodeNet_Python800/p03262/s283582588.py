import math
n, x = map(int,input().split())
p = list(map(int,input().split()))
if n == 1:
    print(abs(p[0]-x))
else:
    g = math.gcd(p[0]-x,p[1]-x)
    for i in range(2,n):
        g = math.gcd(g,p[i]-x)
    print(g)