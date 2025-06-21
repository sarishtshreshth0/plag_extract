import math
from functools import reduce
 
def gcd(ns):
    return reduce(math.gcd, ns)
 
N, X = map(int, input().split())
L = list(map(int, input().split()))
 
diff = [abs(x - X) for x in L]
 
if len(diff) == 1:
    print(diff[0])
else:
    print(gcd(diff))