M, D = map(int, input().split())
count = 0
for m in range(1, M + 1):
    for d in range(10, D + 1):
        d_1 = d % 10
        d_10 = d //10
        count += (d_1 * d_10 == m and d_1 > 1 and d_10 > 1)

print(count)