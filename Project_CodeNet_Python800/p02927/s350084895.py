# coding: utf-8

def is_mul_day(m, d):
    d1 = d % 10
    d10 = d // 10

    if d1 < 2 or d10 < 2:
        return False
    else:
        return m == d1*d10

M, D = list(map(int, input().split()))

res = 0
for i in range(1, M+1):
    for j in range(1, D+1):
        if is_mul_day(i, j):
            res += 1

print(res)