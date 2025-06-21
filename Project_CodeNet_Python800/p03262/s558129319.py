import fractions
from functools import reduce

N, X = map(int, input().split())
L = list(map(int, input().split()))

# move1 = D
# move2 = -D


# D = 1のときは必ずゴールできる
ans = []
# 初期のXとそれ以外の街の差をDで割ったあまりが全て0なら訪れることができる
# つまりそれぞれの街の差を保存し、その最大公約数がDとなる
for i in range(N):
    dfe = abs(L[i] - X)
    ans.append(dfe)

ans = list(set(ans))

# reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]
# functoolsのreduceはある関数があり、それを前の計算結果と重なりを考慮しながら
# 関数に当てはめる、というアクションを繰り返す


def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)


# print(ans)
# print(reduce(lambda x, y: x + y, ans))
print(gcd_list(ans))
