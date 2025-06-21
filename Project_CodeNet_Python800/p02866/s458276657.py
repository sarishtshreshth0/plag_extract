from collections import Counter
N = int(input())
D = list(map(int, input().split()))

c = Counter(D)

mod = 998244353

L = list(set(D[:]))

L.sort(reverse=True)
if (D[0] != 0):
    print(0)
    exit()

if (c[0] > 1):
    print(0)
    exit()

if (N == 1):
    print(1)
    exit()

ans = []
for i in L:
    if (i == 0):
        break
    else:
        ans.append(c[i - 1] ** c[i])

# print(ans)
if (len(ans) == 0):
    print(0)
    exit()

multi_ans = 1
for i in ans:
    multi_ans *= i

print(multi_ans % mod)
