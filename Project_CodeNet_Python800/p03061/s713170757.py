import math
import fractions
from functools import reduce

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

N = int(input())

List = list(map(int,input().split()))

a = List[0]
L = [0 for i in range(N)]
L[0] = a
for i in range(1,N):
  L[i] = gcd(List[i],L[i-1])
  
a = List[-1]
R = [0 for i in range(N)]
R[0] = a
for i in range(1,N):
  R[i] = gcd(List[-i-1],R[i-1])


p = 0
for i in range(N):
  if i == 0:
    ans = R[N-2]
  elif i == N-1:
    ans = L[-2]
  else:
    a = L[i-1]
    b = R[N-i-2]
    ans = gcd(a,b)
  p = max(p,ans)
  
print(int(p))