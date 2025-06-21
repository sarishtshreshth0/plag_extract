n = int(input())
a = [0] + list(map(int, input().split()))

from itertools import accumulate
from collections import Counter

cumsum = list(accumulate(a))
c = Counter(cumsum)

print(sum([(cnt**2 - cnt)//2 for cnt in c.values()]))