import bisect
import math
from functools import reduce

def gcd(A):
    return reduce(math.gcd, A)

N,X = map(int, input().split())
x = sorted(map(int, input().split()))
bisect.insort(x,X)
ans = [x[i+1]-x[i] for i in range(N)] 
if N ==1:
    print(x[1]-x[0])
else:
    print(gcd(ans))