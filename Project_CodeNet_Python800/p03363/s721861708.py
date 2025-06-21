from collections import Counter
from itertools import accumulate
 
n = int(input())
aaa = list(map(int, input().split()))
acc = [0] + list(accumulate(aaa))
agg = Counter(acc)
print(sum(v * (v - 1) // 2 for v in agg.values()))