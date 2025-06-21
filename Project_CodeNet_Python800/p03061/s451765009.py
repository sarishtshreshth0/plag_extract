import sys
input = sys.stdin.readline
from math import gcd

N = int(input())
a = list(map(int, input().split()))
l = [0]

for ai in a:
    l.append(gcd(l[-1], ai))

r = [0]

for ai in a[::-1]:
    r.append(gcd(r[-1], ai))

ans = 0

for i in range(N):
    ans = max(ans, gcd(l[i], r[N-1-i]))

print(ans)