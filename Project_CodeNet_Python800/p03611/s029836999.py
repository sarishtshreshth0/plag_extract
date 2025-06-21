# from pprint import pprint
import math

import collections

n = int(input())
# n, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))

b = [[_a - 1, _a, _a + 1] for _a in a]

numbers = {}
for i in range(n):
    c = collections.Counter(b[i])

    for k, v in c.items():
        if k in numbers.keys():
            numbers[k] += 1
        else:
            numbers.update({k: 1})

ans = sorted(numbers.items(), key=lambda x: x[1], reverse=True)

print(ans[0][1])
