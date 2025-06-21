import sys
import math
from functools import reduce
input = lambda: sys.stdin.readline().rstrip()

N, X = map(int, input().split())

x = list(map(int, input().split()))

x.append(X)
x.sort()

diff = []

for i in range(1, len(x)):
    diff.append(x[i]-x[0])

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

print(gcd_list(diff))