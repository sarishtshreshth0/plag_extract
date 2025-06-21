import itertools
from collections import Counter
import math

N = int(input())
A = list(map(int, input().split()))

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

B = itertools.accumulate(A)
B = [0] + list(B)
C = Counter(B)
ans = 0
for v in C.values():
    if v > 1:
        ans += combinations_count(v, 2)
print(ans)