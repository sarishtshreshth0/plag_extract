# 解説解法

# ちゃんとした括弧列 s=(s1,...,sn):
# - '('と')'の個数は等しい
# - 任意のprefixにおいて，'('の個数 >= ')'の個数 (これがないと閉じない)
#
# di = (s1,...,si)の '('の個数 - ')'の個数
# x = min(d1, ..., dn)
# 
# '('を1つ入れる → dnは1増える xは0 or 1増える (場所による)
# ')'を1つ入れる → dnは1減る xは0 or 1減る (場所による)
#
# 2つの値(a=dn, b=x)を管理する
#
# 4つの操作を考える
#  [a] a += 1
#  [b] a += 1, b += 1
#  [c] a -= 1
#  [d] a -= 1, b -= 1
#
# - b <= 0 から b == 0にしないといけないので，[b]を-b回行う (dはムダなのでやらない)
# - aの値が a + bになっている， a >= bよりa >= 0
# - 次にaを0にしたい．そのため，cを a + b回やる
# - つまり挿入回数は a - 2b = dn - x 回数未満
#
# 構成法
# - 一番左に '(' を -x 回
# - 一番右に ')' を dn - x回

n = int(input())
s = list(input())
# d = []
# co, cc = 0, 0
# for ch in s:
#     if ch == '(':
#         co += 1
#     elif ch == ')':
#         cc += 1
#     d.append(co - cc)

# # 計算
# x = min(d)

# str_left = '(' * (-x)
# str_right = ')' * (d[-1] - x)

# print("{}{}{}".format(str_left, "".join(s), str_right))


co, cc = 0, 0
for ch in s:
    if ch == '(':
        co += 1
    if ch == ')':
        if co > 0:
            co -= 1
        else:
            cc += 1

ans = "(" * cc + "".join(s) + ")" * co
print(ans)