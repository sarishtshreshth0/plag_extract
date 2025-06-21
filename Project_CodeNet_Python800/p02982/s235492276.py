# 少しめんどくさい方法です。
import itertools
n, d = map(int, input().split())
x = []
s = []  # 組み合わせ用の変数。
for i in range(n):
    s.append(i)
    a = list(map(int, input().split()))
    x.append(a)
# 単純に組み合わせで判定する。
ans = 0
for v in itertools.combinations(s, 2):
    t = 0
    # 距離を判定する。
    for i in range(d):
        t += (x[v[0]][i] - x[v[1]][i])**2
    # 少数かどうか？
    if (t**0.5).is_integer():
        ans += 1
print(ans)
