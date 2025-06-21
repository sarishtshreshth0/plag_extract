from functools import reduce
from math import gcd
n,x=map(int,input().split())
L=[abs(x-int(i)) for i in input().split()]
print(reduce(gcd,L))