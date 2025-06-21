q, h, s, d = map(int, input().split())
n = int(input())

qq = 4 * q
hh = 2 * h
# 1リットルの買い方
one = min(qq, min(hh, s))
# 1リットルずつ買う方が安い
if one < d / 2:
    print(n * one)
else:
    print((n // 2) * d + (n % 2) * one)
