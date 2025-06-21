from bisect import bisect_right
from itertools import product


def bisectsearch_right(L, a):
    i = bisect_right(L, a)
    return(i)


N = input()
d = len(N)
N = int(N)
a = [0]*d
for i in range(1, d):
    a[i] = 3**i-3*2**i+3
# print(a)
S = {3, 5, 7}

L = set()
for k in product(S, repeat=d):
    l = set(k)
    if S == l:
        t = [None]*d
        for i in range(d):
            t[i] = str(k[i])
        L.add(int(''.join(t)))
# print(L)
L = list(L)
L.sort()
ct = bisectsearch_right(L, N)
print(sum(a)+ct)
