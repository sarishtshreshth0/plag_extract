import math
from functools import reduce

def gcd(*args):
    return reduce(math.gcd, args)

n, x = map(int, input().split())
city = list(map(int, input().split()))

distance = [abs(c - x) for c in city]

print(gcd(*distance))
