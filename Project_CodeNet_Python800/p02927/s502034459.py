M, D = map(int, input().split())


def check(_m, _d):
    _d_list = list(str(_d))
    if len(_d_list) <= 1:
        d10, d1 = 0, _d
    else:
        d10, d1 = map(int, _d_list)
    if d10 >= 2 and d1 >= 2 and d10 * d1 == _m:
        return 1
    return 0


count = 0
for month in range(1, M+1):
    for day in range(1, D+1):
        count += check(month, day)
print(count)
