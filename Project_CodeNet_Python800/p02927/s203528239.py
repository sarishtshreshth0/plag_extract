months, d = map(int, input().split())

ans_count = 0

for month in range(4, months + 1):
    for i in range(1, d + 1):
        if i <= 9:
            continue

        a, b = map(int, str(i))

        if a >= 2 and b >= 2 and a * b == month:
            ans_count += 1

print(ans_count)