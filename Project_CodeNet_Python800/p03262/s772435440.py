import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

N, X = map(int, input().split())
if N>1: x = [int(_)-X for _ in input().split()]; print(gcd_list(x))
else: x = int(input()) - X; print(abs(x))
