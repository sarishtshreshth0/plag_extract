from itertools import product
from collections import Counter
N = int(input())
res = 0
for k in range(11):
    for p in product([3,5,7],repeat=k):
        if len(Counter(p)) == 3:
            tmp, pw = 0, 1
            for q in p:
                tmp += q*pw
                pw *= 10
            if tmp <= N:
                res += 1
print(res)