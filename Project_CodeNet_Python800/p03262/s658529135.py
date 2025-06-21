n,x,*l=map(int,open(0).read().split())
from math import *
a=0
for i in l: a=gcd(a,abs(i-x))
print(a)