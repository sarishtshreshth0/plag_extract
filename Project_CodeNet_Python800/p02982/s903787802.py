n, d = map(int, input().split())
distances = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(i + 1, n):
        diff_total = 0
        for k in range(d):
            diff = abs(distances[i][k] - distances[j][k])
            diff_total += diff * diff

        flag = False
        for k in range(diff_total + 1):
            if (k * k) == diff_total:
                flag = True
        if flag:
            ans += 1
print(ans)
