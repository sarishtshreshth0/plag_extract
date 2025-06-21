#!/usr/bin/env python3
import sys
import math
import decimal
import itertools
from itertools import product
from functools import reduce
def input():
    return sys.stdin.readline()[:-1]
def gcd(*numbers):
    return reduce(math.gcd, numbers)
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)
def sort_zip(a:list, b:list):
    z = zip(a, b)
    z = sorted(z)
    a, b = zip(*z)
    a = list(a)
    b = list(b)
    return a, b
def ceil(x):
    return math.ceil(x)
def floor(x):
    return math.floor(x)

def main():
    M, D = map(int, input().split())

    ans = 0
    for m in range(1, M + 1):
        for d in range(22, D + 1):
            if int(str(d)[1]) > 1 and int(str(d)[0]) * int(str(d)[1]) == m:
                ans += 1
    print(ans)




if __name__ == '__main__':
    main()
