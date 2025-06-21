from itertools import accumulate
from math import gcd
N = int(input())
*A, = map(int, input().split())

L = list(accumulate(A, gcd))
R = list(accumulate(A[::-1], gcd))[::-1]

ans = max(gcd(l, r) for l, r in zip([0]+L[:-1], R[1:]+[0]))
print(ans)
