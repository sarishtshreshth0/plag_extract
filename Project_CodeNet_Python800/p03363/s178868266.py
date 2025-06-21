from collections import Counter

N = int(input())
numbers = [int(x) for x in input().split()]

cumulatives = [0] * (N + 1)
for i in range(N):
  cumulatives[i + 1] = cumulatives[i] + numbers[i]
  
counter = Counter(cumulatives)

def nC2(n):
  return  n * (n - 1) // 2

print(sum(
  nC2(v)
  for v in counter.values()
  if v > 1
))