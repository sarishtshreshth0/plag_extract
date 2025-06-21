from fractions import gcd

n = int(input().strip())
print((2 * n) // gcd(2, n))
