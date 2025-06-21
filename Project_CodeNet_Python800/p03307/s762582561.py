from fractions import gcd
#最小公倍数
def lcm(a, b):
    return a*b // gcd(a, b)

import sys
input = sys.stdin.readline
N = int(input())
print(lcm(2, N))