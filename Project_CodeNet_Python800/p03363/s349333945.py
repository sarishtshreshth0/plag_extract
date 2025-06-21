from collections import Counter
from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
AA = list(accumulate(A))

def comb(n):
  return n*(n-1)//2

AC = dict(Counter(AA))
answer = 0
if 0 in AC:
  answer = AC[0]

for v in AC.values():
  answer += comb(v)
print(answer)