from functools import reduce
from math import gcd

n,x = map(int, input().split())

A = list(map(int, input().split()))

a = [abs(a-x) for a in A]

print(reduce(gcd,a))