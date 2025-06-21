from itertools import accumulate
from fractions import gcd

N = int(input())
As = list(map(int, input().split()))

cum_gcd = list(accumulate(As, gcd))
cum_rev_gcd = list(accumulate(reversed(As), gcd))[::-1]

max_gcd = max(cum_gcd[-2], cum_rev_gcd[1])
for without in range(1, N-1):
    max_gcd = max(max_gcd, gcd(cum_gcd[without-1], cum_rev_gcd[without+1]))

print(max_gcd)