n = int(input())
li = []
import itertools
for j in range(3,10):
    for i in itertools.product([3,5,7],repeat=j):
        if i.count(3)<1 or i.count(5)<1 or i.count(7)<1:
            pass
        else:
            li += [int(''.join(map(str,i)))]

import bisect
print(bisect.bisect(li,n))