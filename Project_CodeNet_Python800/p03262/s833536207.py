import math
from functools import reduce
 
def gcd(*numbers):
    return reduce(math.gcd, numbers)

N, X = list(map(int, input().split()))
 
x = list(map(int, input().split()))
x.append(X)
x.sort()
 
res = [abs(x[i+1]-x[i]) for i in range(len(x)-1)]
print(gcd(*res))