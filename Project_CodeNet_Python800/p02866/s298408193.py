import sys
readline = sys.stdin.readline

N = int(readline())
D = list(map(int,readline().split()))

counts = [0] * (max(D) + 1)

from collections import Counter
counter = Counter(D)

for k,v in counter.items():
  counts[k] = v

if D[0] != 0 or counts[0] != 1:
  print(0)
  exit(0)
  
ans = 1
DIV = 998244353
for i in range(1, len(counts)):
  ans *= pow(counts[i - 1],counts[i],DIV)
  ans %= DIV

print(ans)