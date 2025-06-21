m, d = map(int, input().split())


def is_seki(m, d1, d10):
    if d1 >= 2 and d10 >= 2 and d1 * d10 == m:
        return 1
    else:
        return 0

total = 0
for month in range(1, m+1):
    for day in range(1, d+1):
        day = str(day)
        if len(day) == 2:
            d1 = int(day[0])
            d10 = int(day[1])
        else:
            d1 = 0
            d10 = int(day)
        total += is_seki(month, d1, d10)

print(total)