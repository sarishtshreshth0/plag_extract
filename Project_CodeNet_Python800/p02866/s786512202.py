from collections import Counter

N = int(input())
A = list(map(int, input().split()))
if A[0] != 0:
  print(0)
  exit()
AC = list(Counter(A).items())
AC.sort()
MOD = 998244353
ans = 1
last_v = 1
last_k = -1
for k, v in AC:
  if k == 0:
    if v != 1:
      print(0)
      exit()
    last_k = 0
    continue
  if k != last_k+1:
    print(0)
    exit()
  ans = ans*pow(last_v, v, MOD)%MOD
  last_v = v
  last_k = k
print(ans)