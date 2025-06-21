m, d = map(int, input().split())
ans = 0
for i in range(1, m + 1):
    for j in range(2, 10):
        if (i % j == 0) & (2 <= i // j <= 9) & (((i // j) * 10 + j) <= d):
            ans += 1
print(ans)            