from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
D = defaultdict(int)

for x in A:
  D[x-1] += 1
  D[x] += 1
  D[x+1] += 1

print(max(D.values()))