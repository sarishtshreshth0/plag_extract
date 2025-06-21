from fractions import gcd
from itertools import accumulate
N = int(input())
A = tuple(map(int, input().split()))
to_right = [0] + list(accumulate(A, gcd))[:-1]
to_left = list(reversed(list(accumulate(reversed(A), gcd))))[1:] + [0]
print(max(gcd(r, l) for r, l in zip(to_right, to_left)))
