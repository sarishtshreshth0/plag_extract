N,X=map(int,input().split())
x=list(map(int,input().split()))

import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

A=[]
for num in x:
    A.append(abs(num-X))

print(gcd_list(A))