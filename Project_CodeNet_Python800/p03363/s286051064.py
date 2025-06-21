import collections

n = int(input())
a = list(map(int, input().split()))

#累積和の計算
s = [0]
for i in range(n):
    s.append(s[i]+a[i])

#条件を満足する部分列をカウント
#累積和のうち，同じものから2つ選ぶ
c = list(collections.Counter(s).items())
ans = 0
for i, j in c:
    if j >= 2:
        ans += j*(j-1)//2

#出力
print(ans)

