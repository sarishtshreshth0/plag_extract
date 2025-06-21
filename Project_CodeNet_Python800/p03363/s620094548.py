from collections import defaultdict
from itertools import accumulate
n = int(input())
A = accumulate(map(int, input().split()))
cnt = defaultdict(int)
cnt[0] += 1
for a in A:
    cnt[a] += 1
print(sum(v*(v-1)//2 for v in cnt.values()))