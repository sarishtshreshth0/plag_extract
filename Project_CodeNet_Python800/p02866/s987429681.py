from collections import Counter


N = int(input())
D = list(map(int, input().split()))
p = 998244353
count = Counter(D)

if D[0] != 0 or len(set(D)) != max(D) + 1 or count[0] > 1:
    ans = 0
else:
    count = sorted(count.items(), key=lambda x: x[0])
    ans = 1
    for i in range(len(count) - 1):
        x = count[i][1]
        y = count[i + 1][1]
        ans *= x ** y
        ans %= p

print(ans)