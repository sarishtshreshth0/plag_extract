m, d = map(int, input().split())
count = 0
for i in range(21, d + 1):
    d1 = i % 10
    d10 = i // 10
    if d10 * d1 <= m and d10 >= 2 and d1 >= 2:
        count += 1
print(count)
