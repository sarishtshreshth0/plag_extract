from collections import Counter
from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
c = Counter()
for i in a:
    for d in [-1, 0, 1]:
        c[i + d] += 1

print(c.most_common()[0][1])
