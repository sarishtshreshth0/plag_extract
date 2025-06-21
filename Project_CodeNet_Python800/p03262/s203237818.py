import math
from functools import reduce

def gcd(*numbers):
  return reduce(math.gcd, numbers)

def gcd_list(numbers):
  return reduce(math.gcd, numbers)

N,X=map(int,input().split())
A=list(map(int,input().split()))
B=[abs(a-X) for a in A]
print(gcd(*B))