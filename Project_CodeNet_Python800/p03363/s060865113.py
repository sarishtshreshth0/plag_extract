from itertools import accumulate
from collections import Counter

n = int(input())
a = list(map(int, input().split()))

acc =  accumulate(a)
counter = Counter(acc)
def cal():
    yield counter[0]
    for v in counter.values():
        if v > 1:
            yield v*(v-1)//2

print(sum(cal()))