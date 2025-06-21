m, d = map(int, input().split())
counter = 0
for mon in range(1, m + 1):
    for day in range(1, d + 1):
        if day >= 22 and int(str(day)[0]) >= 2 and int(str(day)[1]) >= 2:
            if int(str(day)[0]) * int(str(day)[1]) == mon:
                counter += 1
print(counter)
