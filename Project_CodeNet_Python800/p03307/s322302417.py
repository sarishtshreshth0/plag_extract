#!/usr/bin/env python3
from fractions import gcd
n=int(input())
def lcm(m,n):
    return (m*n)//gcd(m,n)
print(lcm(2,n))