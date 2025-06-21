from math import gcd
N,X = map(int,input().split())
g = None
for x in map(int,input().split()):
    if g == None:
        g = x-X
    else:
        g = gcd(g,x-X)
print(abs(g))