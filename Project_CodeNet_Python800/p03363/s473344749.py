from itertools import accumulate
from collections import Counter
N = int(input())
A = list(map(int, input().split()))
S = [0]+list(accumulate(A))
d = Counter(S)
res = 0
for x in d.values():
    res += x*(x-1)//2
print(res)