import copy
from collections import Counter
n = int(input())
a = list(map(int,input().split()))

a_plus1 = copy.copy(a)
a_minus1 = copy.copy(a)
for x in range(n):
    a_plus1[x] += 1
for y in range(n):
    a_minus1[y] -= 1
a_total = a + a_plus1 + a_minus1
cnt = Counter(a_total)
a_max = list(cnt.values())
print(max(a_max))