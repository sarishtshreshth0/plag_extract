#!/usr/bin/env python3
from functools import reduce
from math import gcd

n, X, *x = map(int, open(0).read().split())
x = [abs(i - X) for i in x]
print(reduce(gcd, x))
