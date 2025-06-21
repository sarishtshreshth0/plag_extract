import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
ans = 1
mod = 998244353
D = list(map(int, input().split()))
if D[0] != 0:
    print(0)
    exit()
D = sorted(Counter(D).items())
tmp = D[0][1]
stream = 0
for n, i in D:
    if stream != n:
        print(0)
        exit()
    if n == 0 and i == 1:
        stream += 1
        continue
    elif n==0:
        print(0)
        exit()
    ans *= pow(tmp, i)
    ans %= mod
    tmp = i
    stream += 1
print(ans)
