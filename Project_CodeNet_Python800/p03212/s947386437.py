import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")

from itertools import combinations_with_replacement, permutations, product
n = int(input())
def sub(n):
    s = set()
    for nums in product(*[[3,5,7] for _ in range(n)]):
        if not all(item in nums for item in [3,5,7]):
            continue
        v = 0
        b = 1
        for c in nums:
            v += c*b
            b *= 10
        s.add(v)
    return sorted(list(s))
from bisect import bisect_right as br
l = len(str(n))
ans = 0
for i in range(1, l+1):
    ans += br(sub(i), n)
print(ans)