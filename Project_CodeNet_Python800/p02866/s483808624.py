import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
d = list(map(int, input().split()))
M = 998244353
from collections import Counter
c = Counter(d)
if d[0]!=0 or c[0]>=2:
    ans = 0
else:
    m = max(c.keys())
    ans = 1
    for i in range(1,m+1):
        if i not in c:
            ans = 0
            break
        ans *= pow(c[i-1], c[i], M)
        ans %= M
print(ans%M)