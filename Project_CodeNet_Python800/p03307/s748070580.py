# ABC0102 A - Multiple of 2 and N
from fractions import gcd
n = int(input())
print(2 * n // gcd(2, n))
