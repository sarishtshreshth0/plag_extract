import math
from functools import reduce
N,X = map(int,input().split())
x = list(map(int,input().split()))
y = [abs(i-X) for i in x]
def gcd_list(numbers):
    return reduce(math.gcd, numbers)
print(gcd_list(y))