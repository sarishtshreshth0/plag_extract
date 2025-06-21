from itertools import accumulate
from collections import Counter

N = int(input())
A = list(map(int,input().split()))
S = [0]+list(accumulate(A))
S = Counter(S)
S = list(S.values())
count = 0

for i in range(len(S)):
  count += (S[i]*(S[i]-1)//2)
print(count)