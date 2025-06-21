from itertools import accumulate
from collections import Counter
n, *A = map(int, open(0).read().split())
s = 0
for k, v in Counter(accumulate(A)).items():
    if k == 0:
        s += (v+1)*v // 2
    else:
        s += v*(v-1) // 2
print(s)