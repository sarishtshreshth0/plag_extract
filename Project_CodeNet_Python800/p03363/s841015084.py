import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import itertools
from collections import defaultdict

N,*A = map(int,read().split())

Acum = [0] + list(itertools.accumulate(A))

counter = defaultdict(int)
answer = 0
for x in Acum:
    answer += counter[x]
    counter[x] += 1

print(answer)
