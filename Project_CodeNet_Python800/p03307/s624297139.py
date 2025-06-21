from math import gcd
def solve():
  N = int(input())
  ans = N*2//gcd(2,N)
  return ans
print(solve())