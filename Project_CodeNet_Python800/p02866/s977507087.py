from collections import Counter
N = int(input())
D = list(map(int, input().split()))

ans = 0
cnt = 0
if (D[0]==0) and (D.count(0)==1):
  D = Counter(D)
  cnt = 1
  ans = 1
  for i in range(1, max(D)+1):
    if D[i] == 0:
      ans = 0
      break
    else:
      ans *= cnt ** D[i]
      cnt = D[i]
ans = ans % 998244353
print(ans)