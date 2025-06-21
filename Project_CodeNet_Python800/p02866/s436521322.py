n = int(input())
d = list(map(int, input().split()))

if d[0] != 0:
    print(0)
    exit()

d.sort()
import collections
c = collections.Counter(d)

if c[0] != 1:
    print(0)
    exit()
ans=1
for i in range(1,d[-1]+1):
    if c[i] == 0:
        print(0)
        exit()
    ans*=(c[i-1]**c[i])
    ans%=998244353

print(ans)