from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
a = [0] + a

ans = 0
d = defaultdict(int)
d[0] += 1

for i in range(n):
    #累積和をとる
    a[i + 1] += a[i]
    #nC2を求める
    ans += d[a[i + 1]]
    #登場した回数を数える
    d[a[i + 1]] += 1

print(ans)