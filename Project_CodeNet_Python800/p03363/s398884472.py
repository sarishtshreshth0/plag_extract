n = int(input())
A = list(map(int,input().split()))
S = [0] * (n + 1)

from collections import defaultdict
dic = defaultdict(int)
for i in range(len(A)):
  S[i+1] = S[i] + A[i]
for s in S:
  dic[s] += 1
from scipy.special import comb
ans = 0
for k, v in dic.items():
  if v > 1:
    ans += comb(v, 2, exact=True)

print(int(ans))