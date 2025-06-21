"""
問題文を言い換えると、「最大公約数が最大になるように数字を一つ書き換えろ」ということ。
さらに言い換えると、「最大公約数が最大になるように数字を一つ消せ」ということ。
単純な線形探索でできるか？→NO

最大公約数を小さくする要因となっている数字を一つ消す。
どういう数字が最大公約数を小さくする要因になっているか？
他の数字と共通する素因数が少ない、小さい、次数が小さい。ただ、この3つを総合的に判断するのは難しすぎる。
素因数分解はやめて、単純に約数で探せばよいか。
各Aの約数を昇順で列挙しておく。
まずA1は必ず残すと仮定して、A1の約数の大きい方から順番に、ほかのAの約数になるかどうかを調べる。
その約数を含んでいないAが一つだけ存在するとき、そのAを消せば、その約数が最大公約数となる。

次に、A1を消す場合の最大公約数も求めて、A1を含める場合の最大公約数と比較して大きい方を採用する。
"""

N = int(input())
A = list(map(int,input().split()))

#A1を必ず入れる場合の最大公約数を求める。
yakusu = []

a = A[0]
d = 1
while d*d < a:
    if a % d == 0:
        yakusu.append(d)
        yakusu.append(a//d)
    d += 1
if d*d == a:
    yakusu.append(d)
yakusu.sort(reverse=True)

ans = 1
for v in yakusu:
    cnt = 0
    for i in range(1,N):
        if A[i]%v != 0:
            cnt += 1
    if cnt <= 1:
        ans = v
        break

#A1を入れない場合の最大公約数を求める。
import math
g = A[1]
for i in range(2,N):
    g = math.gcd(g,A[i])

ans = max(ans,g)

print(ans)
