n = int(input())
d = list(map(int, input().split()))

a = [0] * n
for i in range(n):
    a[d[i]] += 1

if a[0] == 1 and d[0] == 0:
    ans = 1
    for i in range(1, n):
        ans *= a[i-1]**a[i]
        ans %= 998244353

    print(ans)
else:
    print(0)