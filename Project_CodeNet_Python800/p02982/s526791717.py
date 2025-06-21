import numpy
from itertools import combinations
N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
c = 0
for x, y in combinations(X, 2):
  s = sum(p**2 for p in numpy.array(x)-numpy.array(y))**.5
  if s.is_integer():
    c += 1
print(c)