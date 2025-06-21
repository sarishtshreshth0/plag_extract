from collections import defaultdict
n = int(input())
lis = list(map(int, input().split()))

mod = 998244353

if lis[0] != 0:
    print(0)
    exit()

d = defaultdict(int)

for i in lis:
    d[i] += 1

if d[0] != 1:
    print(0)
    exit()

ans = 1
for i in range(1, max(lis)+1):
    if i not in d:
        print(0)
        exit()
    ans = ans * (d[i-1]**d[i]) % mod

print(ans)