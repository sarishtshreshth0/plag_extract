from collections import Counter

P = 998244353
N = int(input())
D = [int(x) for x in input().split()]

def solve():
  if D[0] != 0:
    return 0
  total = 1
  max_d = max(D)
  counter = Counter(D)
  if counter[0] != 1:
    return 0
  for i in range(max_d + 1):
    if i not in counter:
      return 0
    if i > 1:
      total *= (counter[i - 1] ** counter[i] % P)
      total %= P
  return total

print(solve())    