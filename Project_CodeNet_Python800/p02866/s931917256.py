import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter

n = int(readline())
d = list(map(int, readline().split()))
counter = Counter(d)
mod = 998244353
ans = 1
if d[0] != 0 or counter[0] != 1:
    print(0)
    exit()
for i in range(1, max(d) + 1):
    ans *= pow(counter[i - 1], counter[i], mod)
    ans %= mod
print(ans)
