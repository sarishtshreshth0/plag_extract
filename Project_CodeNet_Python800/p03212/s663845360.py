import itertools
from collections import Counter
import bisect
N = int(input())

lst = ['3','5','7']
anslst = []
for i in range(1,10):
    for v in itertools.product(lst,repeat=i):
        x = Counter(str(v))
        if x['7'] >= 1 and x['5'] >= 1 and x['3'] >= 1:
            anslst.append(int(''.join(v)))
anslst.sort()
index = bisect.bisect_right(list(anslst), N)
print(index)
