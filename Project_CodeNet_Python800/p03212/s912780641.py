from itertools import product
from bisect import bisect_right
A = []
for i in range(3,10):
    for z in product(("3","5","7"),repeat=i):
        C = {"3":0,"5":0,"7":0}
        for j in range(i):
            C[z[j]] += 1
        if C["3"]>0 and C["5"]>0 and C["7"]>0:
            x = int("".join(z))
            A.append(x)
A = sorted(A)
N = int(input())
ind = bisect_right(A,N)
print(ind)