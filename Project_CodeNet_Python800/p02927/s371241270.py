def seki_day(m, d):
    d10 = d // 10
    d1 = d - d10 * 10

    if d1 >= 2 and m == d10 * d1:
        return 1
    else:
        return 0

M, D = [int(x) for x in input().split()]

count = 0
for m in range(1, M + 1):
    for d in range(22, D + 1):
        count += seki_day(m, d)

print(count)
