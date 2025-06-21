import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

n,x=map(int, input().split())
xn = list(map(int, input().split()))

num_list = [abs(x-xn[i]) for i in range(n)]

Ans = gcd_list(num_list)
print(Ans)