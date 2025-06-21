n = int(input())
ary = list(map(int, input().split()))
#print(n,ary)

ary_2 = [ary[0]]
for i in range(1, n):
    ary_2.append(ary[i] + ary_2[i-1])
ary_2 = [0] + ary_2
#print(ary_2)

from collections import Counter
c = Counter(ary_2)
v = (c.values())
#print(v)

from math import factorial
def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))

ans = 0
for j in v:
    if j >1:
        ans += combinations_count(j,2)

print(ans)