import math
from functools import reduce
n, x = map(int, input().split())
l = list(map(int, input().split()))


def gcd_list(numbers):
    return reduce(math.gcd, numbers)

l_map = list(map(lambda a:abs(a-x), l))
print(gcd_list(l_map))
