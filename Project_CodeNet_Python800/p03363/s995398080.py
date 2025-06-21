import itertools
from collections import Counter
_,*A=map(int,open(0).read().split())
print(sum([v*(v-1)//2 for v in Counter(list(itertools.accumulate([0]+A))).values()]))