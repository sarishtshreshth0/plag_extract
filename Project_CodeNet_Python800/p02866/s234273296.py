from collections import Counter

N = int(input())
D = list(map(int, input().split()))

C = Counter(D)

if D[0] > 0 or C[0] > 1:
  print(0)
  exit(0)
  
mod = int(998244353)
ans = 1
for i in range(2,max(D)+1):
  ans = (ans * (C[i-1] ** C[i]) % mod) % mod
  
print(ans)