N = int(input())
D = list(map(int, input().split()))
M = 998244353
from collections import Counter

if D[0] != 0:
    print(0)
    exit(0)

cd = Counter(D)
if cd[0] != 1:
    print(0)
    exit(0)

tmp = sorted(cd.items(), key=lambda x: x[0])

ans = 1
for kx in range(2, max(D)+1):
# print(tmp)
# for kx in range(2, len(tmp)):
    # print(kx)
    # __, p = tmp[kx-1]
    # _, v = tmp[kx]
    p = cd[kx-1]
    v = cd[kx]
    # print("{}^{}".format(p, v))
    while v > 0:
        ans *= p
        ans %= M
        v -= 1
# print(cd)

# for kx in range(1, max(D)+1):
#     ans *= pow(cd[kx-1], cd[kx],M)
#     ans %= M

print(ans)