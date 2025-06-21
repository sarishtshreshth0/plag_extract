from itertools import accumulate
from collections import Counter
from math import factorial
n = int(input())
a = [0] + list(map(int, input().split()))
b = list(accumulate(a))
c = Counter(b)
d = list(c.values())
ans = 0
for i in d:
    if i >= 2:
        ans += factorial(i) // (factorial(i-2)*2)
print(ans)