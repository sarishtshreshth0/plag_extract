import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)


N, Y = map(int, input().split())
X = list(map(int, input().split()))

X.append(Y)
X2 =sorted(X)
X3 = []

for i in range(1, len(X)):
    X3.append(X2[i] - X2[i-1])

print(gcd_list(X3))
