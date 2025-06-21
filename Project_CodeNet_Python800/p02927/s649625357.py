M, D = map(int, input().split())
cnt = 0
for month in range(1, M+1):
    for day in range(1, D+1):
        tens = day // 10
        ones = day % 10
        if month == tens * ones and tens >= 2 and ones >= 2:
            cnt += 1

print(cnt)